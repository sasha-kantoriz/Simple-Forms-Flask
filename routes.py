from flask import render_template, request, redirect, abort, url_for
from flask_login import login_required
import forms

from models import (
    get_all_members, get_member_by_id,
    add_new_member, add_child_member, add_grandchild_member,
    update_member_by_id, delete_member_by_id,
    get_mother_candidates, get_father_candidates
)
from forms import BaseMemberForm


def index():
    return render_template('main.html')
    # return redirect(url_for('all_members'))


def all_members():
    # member_form = BaseMemberForm()
    if request.method == 'GET':
        # mother_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_mother_candidates(roles=['child', 'adult', 'grand'])]
        # member_form.mother_id.choices = mother_choices
        # father_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_father_candidates(roles=['child', 'adult', 'grand'])]
        # member_form.father_id.choices = father_choices
        # return render_template('index.html', form=member_form, rows=get_all_members())
        return {'members': [dict(m) for m in get_all_members()]}
    elif request.method == 'POST':
        member_data = request.get_json()
        if member_data.get('role') == 'grandchild':
            new_member = add_grandchild_member(role=member_data.get('role'), gender=member_data.get('gender'),
                                               full_name=member_data.get('full_name'),
                                               complete_address=member_data.get('complete_address'),
                                               date_of_birth=member_data.get('date_of_birth'),
                                               place_of_birth=member_data.get('place_of_birth'),
                                               deceased=member_data.get('deceased'),
                                               mother_id=member_data.get('mother_id'), father_id=member_data.get('father_id')
            )
        elif member_data.get('role') == 'child':
            new_member = add_child_member(role=member_data.get('role'), gender=member_data.get('gender'),
                                          full_name=member_data.get('full_name'), complete_address=member_data.get('complete_address'),
                                          date_of_birth=member_data.get('date_of_birth'), place_of_birth=member_data.get('place_of_birth'),
                                          deceased=member_data.get('deceased'),
                                          mother_id=member_data.get('mother_id'), father_id=member_data.get('father_id'),
                                          spouse_full_name=member_data.get('spouse_full_name'),
                                          spouse_date_of_birth=member_data.get('spouse_date_of_birth'),
                                          spouse_place_of_birth=member_data.get('spouse_place_of_birth'),
                                          inlaws_full_name=member_data.get('inlaws_full_name'),
                                          father_inlaws_full_address=member_data.get('father_inlaws_full_address'),
                                          father_inlaws_deceased=member_data.get('father_inlaws_deceased')
            )
        else:
            new_member = add_new_member(role=member_data.get('role'), gender=member_data.get('gender'),
                                        full_name=member_data.get('full_name'), complete_address=member_data.get('complete_address'),
                                        date_of_birth=member_data.get('date_of_birth'), place_of_birth=member_data.get('place_of_birth'),
                                        deceased=member_data.get('deceased'),
                                        spouse_full_name=member_data.get('spouse_full_name'),
                                        spouse_date_of_birth=member_data.get('spouse_date_of_birth'),
                                        spouse_place_of_birth=member_data.get('spouse_place_of_birth'),
                                        inlaws_full_name=member_data.get('inlaws_full_name'),
                                        father_inlaws_full_address=member_data.get('father_inlaws_full_address'),
                                        father_inlaws_deceased=member_data.get('father_inlaws_deceased'),
                                        mother_id=member_data.get('mother_id'), father_id=member_data.get('father_id'),
            )
        return redirect(url_for('all_members'))


def member_by_id(_id):
    member_form = BaseMemberForm()
    if request.method == 'GET':
        mother_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_mother_candidates(roles=['child', 'adult', 'grand'])]
        member_form.mother_id.choices = mother_choices
        father_choices = [(None, 'None')] + [(c.id, c.full_name) for c in get_father_candidates(roles=['child', 'adult', 'grand'])]
        member_form.father_id.choices = father_choices
        return render_template('modify_user.html', form=member_form, member=get_member_by_id(_id), getattr=getattr)
    if request.method == 'POST':
        update_member_by_id(_id=_id, role=member_form.role.data, gender=member_form.gender.data,
                            full_name=member_form.full_name.data,
                            complete_address=member_form.complete_address.data,
                            date_of_birth=member_form.date_of_birth.data,
                            place_of_birth=member_form.place_of_birth.data,
                            deceased=member_form.deceased.data,
                            spouse_full_name=member_form.spouse_full_name.data,
                            spouse_date_of_birth=member_form.spouse_date_of_birth.data,
                            spouse_place_of_birth=member_form.spouse_place_of_birth.data,
                            inlaws_full_name=member_form.inlaws_full_name.data,
                            father_inlaws_full_address=member_form.father_inlaws_full_address.data,
                            father_inlaws_deceased=member_form.father_inlaws_deceased.data
        )
        return redirect(url_for('all_members'))


def delete_member(_id):
    delete_member_by_id(_id)
    return redirect(url_for('all_members'))


def get_children(_id):
    parent = get_member_by_id(_id)
    children = parent.fchildren if parent.gender == 'male' else parent.mchildren
    return render_template('relationships.html', rows=children)


def get_parents(_id):
    child = get_member_by_id(_id)
    parents = []
    if child.mother:
        parents.append(child.mother)
    if child.father:
        parents.append(child.father)
    return render_template('relationships.html', rows=parents)


def get_grandchildren(_id):
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
        if grandchild.father.father:
            grandparents.append(grandchild.father.father)
    return render_template('relationships.html', rows=grandparents)


def get_grandgrand_children(_id):
    grandparent = get_member_by_id(_id)
    grandchildren = []
    if grandparent.gender == 'male':
        for adult in grandparent.fchildren:
            if adult.gender == 'male':
                for grandchild in adult.fchildren:
                    if grandchild.gender == 'male':
                        grandchildren.extend(grandchild.fchildren)
                    else:
                        grandchildren.extend(grandchild.mchildren)
            else:
                for grandchild in adult.mchildren:
                    if grandchild.gender == 'male':
                        grandchildren.extend(grandchild.fchildren)
                    else:
                        grandchildren.extend(grandchild.mchildren)
    else:
        for child in grandparent.mchildren:
            if child.gender == 'male':
                grandchildren.extend(child.fchildren)
            else:
                grandchildren.extend(child.mchildren)
    return render_template('relationships.html', rows=grandchildren)


def get_grandgrand_parents(_id):
    grandchild = get_member_by_id(_id)
    grandparents = []
    if grandchild.mother:
        if grandchild.mother.mother:
            if grandchild.mother.mother.mother:
                grandparents.append(grandchild.mother.mother.mother)
            if grandchild.mother.mother.father:
                grandparents.append(grandchild.mother.mother.father)
        if grandchild.mother.father:
            if grandchild.mother.father.mother:
                grandparents.append(grandchild.mother.father.mother)
            if grandchild.mother.father.father:
                grandparents.append(grandchild.mother.father.father)
    if grandchild.father:
        if grandchild.father.mother:
            if grandchild.father.mother.mother:
                grandparents.append(grandchild.father.mother.mother)
            if grandchild.father.mother.father:
                grandparents.append(grandchild.father.mother.father)
        if grandchild.father.father:
            if grandchild.father.father.mother:
                grandparents.append(grandchild.father.father.mother)
            if grandchild.father.father.father:
                grandparents.append(grandchild.father.father.father)
    return render_template('relationships.html', rows=grandparents)


def get_parents_candidates():
    role, roles = request.args.get('role', None), list()
    response = {
        'female': [],
        'male': [],
    }
    if role is None:
        roles = ['grand', 'adult', 'child', 'grandchild']
    elif role == 'grand':
        roles = [None]
    elif role == 'adult':
        roles = ['grand']
    elif role == 'child':
        roles = ['grand', 'adult']
    elif role == 'grandchild':
        roles = ['grand', 'adult', 'child']
    response['female'] = [{'value': c.id, 'title': c.full_name} for c in get_mother_candidates(roles)]
    response['male'] = [{'value': c.id, 'title': c.full_name} for c in get_father_candidates(roles)]
    return response
