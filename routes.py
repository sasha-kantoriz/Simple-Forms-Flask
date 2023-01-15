from flask import render_template, request, redirect, abort, url_for
from flask_login import login_required
import forms

from models import (
    get_all_members, get_member_by_id,
    add_new_member, add_child_member,
    update_member_by_id, delete_member,
    get_mother_candidates, get_father_candidates
)
from forms import BaseMemberForm


def index():
    return redirect(url_for('all_members'))


def all_members():
    member_form = BaseMemberForm()
    if request.method == 'GET':
        mother_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_mother_candidates(roles=['adult', 'grand'])]
        member_form.mother_id.choices = mother_choices
        father_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_father_candidates(roles=['adult', 'grand'])]
        member_form.father_id.choices = father_choices
        return render_template('index.html', form=member_form, rows=get_all_members())
    elif request.method == 'POST':
        if member_form.role.data == 'child':
            new_member = add_child_member(role=member_form.role.data, gender=member_form.gender.data,
                                          full_name=member_form.full_name.data, complete_address=member_form.complete_address.data,
                                          date_of_birth=member_form.date_of_birth.data, place_of_birth=member_form.place_of_birth.data,
                                          deceased=member_form.deceased.data,
                                          mother_id=member_form.mother_id.data, father_id=member_form.father_id.data
            )
        elif member_form.role.data == 'adult':
            if member_form.gender.data == 'male':
                new_member = add_new_member(role=member_form.role.data, gender=member_form.gender.data,
                                            full_name=member_form.full_name.data, complete_address=member_form.complete_address.data,
                                            date_of_birth=member_form.date_of_birth.data, place_of_birth=member_form.place_of_birth.data,
                                            deceased=member_form.deceased.data,
                                            mother_id=member_form.mother_id.data, father_id=member_form.father_id.data,
                                            wifes_full_name=member_form.wifes_full_name.data,
                                            inlaws_full_name=member_form.inlaws_full_name.data,
                                            father_inlaws_full_address=member_form.father_inlaws_full_address.data
                )
            else:
                new_member = add_new_member(role=member_form.role.data, gender=member_form.gender.data,
                                            full_name=member_form.full_name.data,
                                            complete_address=member_form.complete_address.data,
                                            date_of_birth=member_form.date_of_birth.data,
                                            place_of_birth=member_form.place_of_birth.data,
                                            deceased=member_form.deceased.data,
                                            mother_id=member_form.mother_id.data, father_id=member_form.father_id.data,
                                            husbands_full_name=member_form.husbands_full_name.data,
                                            inlaws_full_name=member_form.inlaws_full_name.data,
                                            father_inlaws_full_address=member_form.father_inlaws_full_address.data
                )
        else:
            if member_form.gender.data == 'male':
                new_member = add_new_member(role=member_form.role.data, gender=member_form.gender.data,
                                            full_name=member_form.full_name.data, complete_address=member_form.complete_address.data,
                                            date_of_birth=member_form.date_of_birth.data, place_of_birth=member_form.place_of_birth.data,
                                            deceased=member_form.deceased.data,
                                            wifes_full_name=member_form.wifes_full_name.data,
                                            inlaws_full_name=member_form.inlaws_full_name.data,
                                            father_inlaws_full_address=member_form.father_inlaws_full_address.data
                )
            else:
                new_member = add_new_member(role=member_form.role.data, gender=member_form.gender.data,
                                            full_name=member_form.full_name.data,
                                            complete_address=member_form.complete_address.data,
                                            date_of_birth=member_form.date_of_birth.data,
                                            place_of_birth=member_form.place_of_birth.data,
                                            deceased=member_form.deceased.data,
                                            husbands_full_name=member_form.husbands_full_name.data,
                                            inlaws_full_name=member_form.inlaws_full_name.data,
                                            father_inlaws_full_address=member_form.father_inlaws_full_address.data
                )
        return dict(new_member)


def member_by_id(_id):
    member_form = BaseMemberForm()
    if request.method == 'GET':
        mother_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_mother_candidates(roles=['adult', 'grand'])]
        member_form.mother_id.choices = mother_choices
        father_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_father_candidates(roles=['adult', 'grand'])]
        member_form.father_id.choices = father_choices
        return render_template('modify_user.html', form=member_form, member=get_member_by_id(_id), getattr=getattr)
    if request.method == 'POST':
        update_member_by_id(_id=_id, role=member_form.role.data, gender=member_form.gender.data,
                            full_name=member_form.full_name.data,
                            complete_address=member_form.complete_address.data,
                            date_of_birth=member_form.date_of_birth.data,
                            place_of_birth=member_form.place_of_birth.data,
                            deceased=member_form.deceased.data,
                            husbands_full_name=member_form.husbands_full_name.data,
                            inlaws_full_name=member_form.inlaws_full_name.data,
                            father_inlaws_full_address=member_form.father_inlaws_full_address.data
        )
        return redirect(url_for('all_members'))


def delete_member(_id):
    delete_member(_id)
    return redirect(url_for('all_members'))


def get_children(_id):
    from models import get_member_by_id
    parent = get_member_by_id(_id)
    children = parent.fchildren if parent.gender == 'male' else parent.mchildren
    return render_template('relationships.html', rows=children)


def get_parents(_id):
    from models import get_member_by_id
    child = get_member_by_id(_id)
    parents = []
    if child.mother:
        parents.append(child.mother)
    if child.father:
        parents.append(child.father)
    return render_template('relationships.html', rows=parents)


def get_grandchildren(_id):
    from models import get_member_by_id
    parent = get_member_by_id(_id)
    grandchildren = []
    if parent.gender == 'male':
        for child in parent.fchildren:
            if child.gender == 'male':
                grandchildren.extend(child.fchildren)
            else:
                grandchildren.extend(child.mchildren)
    else:
        for child in parent.mchildren:
            if child.gender == 'male':
                grandchildren.extend(child.fchildren)
            else:
                grandchildren.extend(child.mchildren)
    return render_template('relationships.html', rows=grandchildren)


def get_grandparents(_id):
    from models import get_member_by_id
    grandchild = get_member_by_id(_id)
    grandparents = []
    if grandchild.mother:
        if grandchild.mother.mother:
            grandparents.append(grandchild.mother.mother)
        if grandchild.mother.father:
            grandparents.append(grandchild.mother.father)
    if grandchild.father:
        if grandchild.father.mother:
            grandparents.append(grandchild.father.mother)
        if grandchild.mother.mother:
            grandparents.append(grandchild.father.father)
    return render_template('relationships.html', rows=grandparents)
