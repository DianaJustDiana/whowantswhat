from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.shortcuts import redirect


from .forms import CreateAFamilyForm, AddMembersForm

from .models import Family, Member


# Need for @login required decorator.
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required sends unvalidated users to url of my choosing. In this case, the home page.
# TODO When the user creates a family group, the user is the parent of that group.
# Should the user be added as a member as well?


@login_required(login_url='/')
def create_a_family(request):
    """User can create a family group."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CreateAFamilyForm()
    else:
        # POST data submitted; process data.
        form = CreateAFamilyForm(request.POST)

        if form.is_valid():
            # Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)
            # Here's where I can add extra data and make the object's parent the current user.
            # This makes the user creating a family group the parent of that group.
            form.parent = request.user
            # Then save again for real.
            form.save()

            # TODO Change this so after user creates a family group, redirect user to add members form.
            # return HttpResponseRedirect(reverse('family_groups:add_members'))
            return redirect('family_groups:add_members')

    context = {'form': form}
    return render(request, 'family_groups/create_a_family.html', context)

# @login_required sends unvalidated users to url of my choosing. In this case, the home page.
# TODO Limit this! Available only to a user who is already a parent to a group.


@login_required(login_url='/')
def add_members(request):
    """Parent of family group can add members."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        # Need to add this back if I want the current user to be the one taking action.
        # trying something
        form = AddMembersForm(request.user)
        # end trying something
        # And need to remove this.
        #form = AddMembersForm()
    else:
        # Need to add this back if I want the current user to be the one taking action.
        ##form = AddMembersForm(request.POST, current_user=request.user)
        # And need to remove this.
        # The order here is IMPORTANT. The user part has to come first.
        form = AddMembersForm(request.user, request.POST)

        if form.is_valid():
            # Saving the form with commit=False generates an object called "form."
            form = form.save(commit=False)
            # Here's where I can add extra data and make the object belong to the family group.
            current_user = request.user
            #print("This is the current user:")
            # print(current_user)
# trying something
            all_my_family_groups = Family.objects.filter(parent=current_user)
# end trying something
            #current_family = Family.objects.get(parent=current_user)
            current_family = form.family
            # print("This is the current family group:"
            # print(current_family)
            test_this_member = form.name
            # Get all the members already in this family group.
            #list_of_members = Family.objects.get(parent=current_user)
            #print("This is the list of members:")
            # print(list_of_members)
            # See if the member the current user wants to add is already in the family group.
            already_a_member = current_family.member_set.filter(
                name=test_this_member)
            #print("Checking this member:")
            # print(test_this_member)
            # print(already_a_member)
            #print("The parent of this group:")
            # print(current_family.parent)
            # See if the member the current user wants to add IS the current user.
            # TODO Prevent family parent from adding self as member.
            if already_a_member or (test_this_member == current_user):
                # TODO Tell user this member already is part of the family group.
                #flash("I'm sorry, but that username is already taken.", 'error')
                #print("ALREADY A MEMBER OF THIS FAMILY GROUP")
                # return HttpResponseRedirect(reverse('family_groups:add_members'))
                return redirect('family_groups:add_members')
            else:
                # Makes existing family group the one the new member is added to.
                form.family = current_family
                # print(form.family)
                form = form.save()
                # After user addes new offer, redirect user to offers index page.
                # return HttpResponseRedirect(reverse('offers:index'))
                return redirect('offers:index')

            # TODO end test this out
    context = {
        'form': form,
        # 'all_my_family_groups': all_my_family_groups,
    }

    return render(request, 'family_groups/add_members.html', context)

# Should be a GET request. That's the default, so no need to specify.
# @login_required sends unvalidated users to url of my choosing. In this case, the home page.


@login_required(login_url='/')
def index(request):
    """Will display index of parent's family and the family members."""
    current_user = request.user
    # If current user is parent to a family group, this will gather them.
    # TODO Why is this broken? If current user is NOT a parent, this throws an error.
    # .values('member__name__username', 'family_name', 'parent__username')
    my_family_groups = Family.objects.filter(parent=current_user)
    print("my family group(s)")
    print(my_family_groups)

    # TODO Marking this QuerySet so I can find it easily. Important part is member_set.
    # Adding condition so if there are no family groups the variable f never enters the picture.
    # if my_family_groups:
    # for each in my_family_groups:
    #    members = each.member_set.all()
    #    family_name = each.family_name
    #    parent = each.parent

    # Need this because next part with context variables needs something for members.
    # else:
    #    family_name = "No family group yet"
    #    members = None
    #    parent = None

    # Context is the dictionary of info that populates the family_groups/index template.
    context = {
        "title": "My family groups",
        "family_groups": my_family_groups,
        # "members": members,
        # "parent": parent,
    }

    return render(request, 'family_groups/index.html', context)
