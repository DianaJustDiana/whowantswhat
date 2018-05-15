from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateAFamilyForm, AddMembersForm

from .models import Family, Member, User


#Need for @login required decorator.
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required sends unvalidated users to url of my choosing. In this case, the home page.    
@login_required(login_url='/')  
def create_a_family(request):
    """User can create a family group."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = CreateAFamilyForm()
    else:
        #POST data submitted; process data.
        form = CreateAFamilyForm(request.POST)

        if form.is_valid():
            #Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)       
            #Here's where I can add extra data and make the object's parent the current user. 
            current_user = request.user
            #This changes boolean to True so I can use .is_parent to shield some views.
            #TODO Ask Brian to look at this.
            current_user.is_parent = True        
            #This makes the user creating a family group the parent of that group.
            form.parent = current_user
            #Then save again for real.
            form.save()
            #TODO Remove this once the custom template tag is working.
            print(current_user.is_parent)
            #TODO Change this so after user creates a family group, redirect user to add members form.
            return HttpResponseRedirect(reverse('family_groups:add_members'))

    context = {'form': form}
    return render(request, 'family_groups/create_a_family.html', context) 

#@login_required sends unvalidated users to url of my choosing. In this case, the home page.  
#TODO Limit this! Available only to a user who is already a parent to a group.  
@login_required(login_url='/')  
def add_members(request):
    """Parent of family group can add members."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = AddMembersForm()
    else:
        form = AddMembersForm(request.POST)

        if form.is_valid():
             #Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)    
            #Here's where I can add extra data and make the object belong to the family group.
            current_user = request.user
            #print("This is the current user:")
            #print(current_user)
            #current_family = Family.objects.get(parent=current_user)
            #print("This is the current family group:")
            #print(current_family)
            test_this_member = form.name
            #TODO test this out
            #print("This should be the current family group, too:")

            #TODO Marking this QuerySet so I can find it easily. Important part is member_set.
            current_family = Family.objects.get(parent=current_user)
            already_a_member = current_family.member_set.get(name=test_this_member)

            #See if member being added in form already exists in family group.
            if already_a_member:
                #Tell user they already exist in family group.
                #flash("I'm sorry, but that username is already taken.", 'error')
                print("ALREADY A MEMBER OF THIS FAMILY GROUP")
                #return redirect('/signup')

            else:

                form.family = current_family
                print(form.family)
                form = form.save()
                #After user addes new offer, redirect user to offers index page.
                return HttpResponseRedirect(reverse('offers:index'))
            
            #TODO end test this out
    
    context = {'form': form}
    return render(request, 'family_groups/add_members.html', context) 

#Should be a GET request. That's the default, so no need to specify.
#@login_required sends unvalidated users to url of my choosing. In this case, the home page.
@login_required(login_url='/')
def index(request):
    """Will display index of parent's family and the family members."""
    current_user = request.user
    #If current user is parent to a family group, this will gather them.
    #TODO Why is this broken? If current user is NOT a parent, this throws an error.
    list_of_family_groups = Family.objects.filter(parent=current_user)
    #TODO Remove after testing.
    print("NOTHING HERE")

    #TODO Marking this QuerySet so I can find it easily. Important part is member_set.
    #Adding condition so if there are no family groups the variable f never enters the picture.
    if list_of_family_groups:
        f = Family.objects.get(parent=current_user)
        members = f.member_set.all()
    #Need this because next part with context variables needs something for members.
    else:
        members = None

    #Context is the dictionary of info that populates the family_groups/index template.
    context = {
        "title": "My family groups",
        "family_groups": list_of_family_groups,
        "members": members,
    }

    return render(request, 'family_groups/index.html', context)
    
    
    