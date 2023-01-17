from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Member(db.Model):
    __tablename__ = 'Members'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    full_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.String(50))
    place_of_birth = db.Column(db.String(1000))
    complete_address = db.Column(db.String(1000))
    deceased = db.Column(db.Boolean, default=False)
    #
    spouse_full_name = db.Column(db.String(1000), nullable=True)
    spouse_date_of_birth = db.Column(db.String(50), nullable=True)
    spouse_place_of_birth = db.Column(db.String(1000), nullable=True)
    inlaws_full_name = db.Column(db.String(1000), nullable=True)
    father_inlaws_deceased = db.Column(db.Boolean, nullable=True)
    father_inlaws_full_address = db.Column(db.String(1000), nullable=True)
    #
    mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    mother = db.relationship('Member', remote_side=[id], backref='mchildren', foreign_keys=[mother_id])
    father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    father = db.relationship('Member', remote_side=[id], backref='fchildren', foreign_keys=[father_id])
    #
    grandmother_by_mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandmother_by_mother = db.relationship('Member', remote_side=[id], backref='mmgrandchildren', foreign_keys=[grandmother_by_mother_id])
    grandfather_by_mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandfather_by_mother = db.relationship('Member', remote_side=[id], backref='fmgrandchildren', foreign_keys=[grandfather_by_mother_id])
    grandmother_by_father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandmother_by_father = db.relationship('Member', remote_side=[id], backref='mfgrandchildren', foreign_keys=[grandmother_by_father_id])
    grandfather_by_father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandfather_by_father = db.relationship('Member', remote_side=[id], backref='ffgrandchildren', foreign_keys=[grandfather_by_father_id])
    #
    grandmother_by_grandmother_by_mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandmother_by_grandmother_by_mother = db.relationship('Member', remote_side=[id], backref='mmmgrandchildren',
                                                           foreign_keys=[grandmother_by_grandmother_by_mother_id])
    grandfather_by_grandmother_by_mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandfather_by_grandmother_by_mother = db.relationship('Member', remote_side=[id], backref='fmmgrandchildren',
                                                           foreign_keys=[grandfather_by_grandmother_by_mother_id])
    grandmother_by_grandfather_by_mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandmother_by_grandfather_by_mother = db.relationship('Member', remote_side=[id], backref='mfmgrandchildren',
                                                           foreign_keys=[grandmother_by_grandfather_by_mother_id])
    grandfather_by_grandfather_by_mother_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandfather_by_grandfather_by_mother = db.relationship('Member', remote_side=[id], backref='ffmgrandchildren',
                                                           foreign_keys=[grandfather_by_grandfather_by_mother_id])
    grandmother_by_grandmother_by_father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandmother_by_grandmother_by_father = db.relationship('Member', remote_side=[id], backref='mmfgrandchildren',
                                                           foreign_keys=[grandmother_by_grandmother_by_father_id])
    grandfather_by_grandmother_by_father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandfather_by_grandmother_by_father = db.relationship('Member', remote_side=[id], backref='fmfgrandchildren',
                                                           foreign_keys=[grandfather_by_grandmother_by_father_id])
    grandmother_by_grandfather_by_father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandmother_by_grandfather_by_father = db.relationship('Member', remote_side=[id], backref='mffgrandchildren',
                                                           foreign_keys=[grandmother_by_grandfather_by_father_id])
    grandfather_by_grandfather_by_father_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=True)
    grandfather_by_grandfather_by_father = db.relationship('Member', remote_side=[id], backref='fffgrandchildren',
                                                           foreign_keys=[grandfather_by_grandfather_by_father_id])

    def __iter__(self):
        return iter(
            [
                ('id', self.id),
                ('role', self.role),
                ('gender', self.gender),
                ('full_name', self.full_name),
                ('date_of_birth', self.date_of_birth),
                ('place_of_birth', self.place_of_birth),
                ('complete_address', self.complete_address),
                ('deceased', self.deceased),
                ('spouse_full_name', self.spouse_full_name),
                ('spouse_date_of_birth', self.spouse_date_of_birth),
                ('spouse_place_of_birth', self.spouse_place_of_birth),
                ('inlaws_full_name', self.inlaws_full_name),
                ('father_inlaws_full_address', self.father_inlaws_full_address),
                ('father_inlaws_deceased', self.father_inlaws_deceased),
                # ('mother', dict(self.mother) if self.mother else None),
                # ('father', dict(self.father) if self.father else None),
                # ('grandmother_by_mother', dict(self.grandmother_by_mother) if self.grandmother_by_mother else None),
                # ('grandmother_by_father', dict(self.grandmother_by_father) if self.grandmother_by_father else None),
                # ('grandfather_by_mother', dict(self.grandfather_by_mother) if self.grandfather_by_mother else None),
                # ('grandfather_by_father', dict(self.grandfather_by_father) if self.grandfather_by_father else None),
                # ('mchildren', [dict(child) for child in self.mchildren]),
                # ('fchildren', [dict(child) for child in self.fchildren]),
                # ('mmgrandchildren', [dict(child) for child in self.mmgrandchildren]),
                # ('mfgrandchildren', [dict(child) for child in self.mfgrandchildren]),
                # ('fmgrandchildren', [dict(child) for child in self.fmgrandchildren]),
                # ('ffgrandchildren', [dict(child) for child in self.ffgrandchildren])
            ]
        )


def add_new_member(role=None, gender=None, full_name=None,
                   date_of_birth=None, place_of_birth=None,
                   complete_address=None, deceased=None,
                   spouse_full_name=None, spouse_date_of_birth=None, spouse_place_of_birth=None,
                   inlaws_full_name=None, father_inlaws_full_address=None, father_inlaws_deceased=None,
                   mother_id=None, father_id=None
    ):
    new_member = Member(role=role, gender=gender, full_name=full_name,
                        date_of_birth=date_of_birth, place_of_birth=place_of_birth,
                        complete_address=complete_address, deceased=deceased,
                        spouse_full_name=spouse_full_name, spouse_date_of_birth=spouse_date_of_birth, spouse_place_of_birth=spouse_place_of_birth,
                        inlaws_full_name=inlaws_full_name, father_inlaws_full_address=father_inlaws_full_address, father_inlaws_deceased=father_inlaws_deceased,
                        mother_id=mother_id, father_id=father_id
    )
    db.session.add(new_member)
    db.session.commit()
    return new_member


def get_all_members():
    return Member.query.all()


def get_member_by_id(_id):
    member = Member.query.filter_by(id=_id).first()
    if member:
        return member


def get_mother_candidates(roles):
    return Member.query.filter(Member.role.in_(roles)).filter_by(gender='female').all()


def get_father_candidates(roles):
    return Member.query.filter(Member.role.in_(roles)).filter_by(gender='male').all()


def update_member_by_id(_id, role=None, gender=None, full_name=None,
                        date_of_birth=None, place_of_birth=None,
                        complete_address=None, deceased=None,
                        spouse_full_name=None, spouse_date_of_birth=None, spouse_place_of_birth=None,
                        inlaws_full_name=None, father_inlaws_full_address=None, father_inlaws_deceased=None,
                        mother_id=None, father_id=None,
                        grandmother_by_mother_id=None, grandmother_by_father_id=None,
                        grandfather_by_mother_id=None, grandfather_by_father_id=None,
                        grandmother_by_grandmother_by_mother_id=None, grandfather_by_grandmother_by_mother_id=None,
                        grandmother_by_grandfather_by_mother_id=None, grandfather_by_grandfather_by_mother_id=None,
                        grandmother_by_grandmother_by_father_id=None, grandfather_by_grandmother_by_father_id=None,
                        grandmother_by_grandfather_by_father_id=None, grandfather_by_grandfather_by_father_id=None
    ):
    member = Member.query.filter_by(id=_id).first()
    if role:
        member.role = role
    if gender:
        member.gender = gender
    if full_name:
        member.full_name = full_name
    if date_of_birth:
        member.date_of_birth = date_of_birth
    if place_of_birth:
        member.place_of_birth = place_of_birth
    if complete_address:
        member.complete_address = complete_address
    if deceased:
        member.deceased = deceased
    if spouse_full_name:
        member.spouse_full_name = spouse_full_name
    if spouse_date_of_birth:
        member.spouse_full_name = spouse_full_name
    if spouse_place_of_birth:
        member.spouse_place_of_birth = spouse_place_of_birth
    if inlaws_full_name:
        member.inlaws_full_name = inlaws_full_name
    if father_inlaws_full_address:
        member.father_inlaws_full_address = father_inlaws_full_address
    if father_inlaws_deceased:
        member.father_inlaws_deceased = father_inlaws_deceased
    if mother_id:
        mother = Member.query.filter_by(id=mother_id).first()
        if mother:
            member.mother_id = mother_id
            if mother.mother:
                member.grandmother_by_mother_id = mother.mother.id
                # by mother grandmother
                if mother.mother.mother:
                    member.grandmother_by_grandmother_by_mother_id = mother.mother.mother.id
                if mother.mother.father:
                    member.grandfather_by_grandmother_by_mother_id = mother.mother.father.id
            if mother.father:
                member.grandfather_by_mother_id = mother.father.id
                # by mother grandfather
                if mother.father.mother:
                    member.grandmother_by_grandfather_by_mother_id = mother.father.mother.id
                if mother.father.father:
                    member.grandfather_by_grandfather_by_mother_id = mother.father.father.id
    if father_id:
        father = Member.query.filter_by(id=father_id).first()
        if father:
            member.father_id = father_id
            if father.mother:
                member.grandmother_by_father_id = father.mother.id
                # by father grandmother
                if father.mother.mother:
                    member.grandmother_by_grandmother_by_father_id = father.mother.mother.id
                if mother.mother.father:
                    member.grandfather_by_grandmother_by_father_id = father.mother.father.id
            if father.father:
                member.grandfather_by_father_id = father.father.id
                # by father grandfather
                if mother.father.mother:
                    member.grandmother_by_grandfather_by_father_id = father.father.mother.id
                if mother.father.father:
                    member.grandfather_by_grandfather_by_father_id = father.father.father.id
    #
    if grandmother_by_mother_id:
        member.grandmother_by_mother_id = grandmother_by_mother_id
    if grandmother_by_father_id:
        member.grandmother_by_father_id = grandmother_by_father_id
    if grandfather_by_mother_id:
        member.grandfather_by_mother_id = grandfather_by_mother_id
    if grandfather_by_father_id:
        member.grandfather_by_father_id = grandfather_by_father_id
    #
    if grandmother_by_grandmother_by_mother_id:
        member.grandmother_by_grandmother_by_mother_id = grandmother_by_grandmother_by_mother_id
    if grandfather_by_grandmother_by_mother_id:
        member.grandfather_by_grandmother_by_mother_id = grandfather_by_grandmother_by_mother_id
    if grandmother_by_grandfather_by_mother_id:
        member.grandmother_by_grandfather_by_mother_id = grandmother_by_grandfather_by_mother_id
    if grandfather_by_grandfather_by_mother_id:
        member.grandfather_by_grandfather_by_mother_id = grandfather_by_grandfather_by_mother_id
    if grandmother_by_grandmother_by_father_id:
        member.grandmother_by_grandmother_by_father_id = grandmother_by_grandmother_by_father_id
    if grandfather_by_grandmother_by_father_id:
        member.grandfather_by_grandmother_by_father_id = grandfather_by_grandmother_by_father_id
    if grandmother_by_grandfather_by_father_id:
        member.grandmother_by_grandfather_by_father_id = grandmother_by_grandfather_by_father_id
    if grandfather_by_grandfather_by_father_id:
        member.grandfather_by_grandfather_by_father_id = grandfather_by_grandfather_by_father_id
    db.session.commit()
    return member


def delete_member_by_id(_id):
    member = Member.query.filter_by(id=_id).first()
    db.session.delete(member)
    db.session.commit()


def add_child_member(role=None, gender=None, full_name=None,
                     date_of_birth=None, place_of_birth=None,
                     complete_address=None, deceased=None,
                     spouse_full_name=None, spouse_date_of_birth=None, spouse_place_of_birth=None,
                     inlaws_full_name=None, father_inlaws_full_address=None, father_inlaws_deceased=None,
                     mother_id=None, father_id=None
    ):
    grandmother_by_mother_id = None
    grandfather_by_mother_id = None
    grandmother_by_father_id = None
    grandfather_by_father_id = None
    mother = Member.query.filter_by(id=mother_id).first()
    if mother:
        if mother.mother:
            grandmother_by_mother_id = mother.mother.id
        if mother.father:
            grandfather_by_mother_id = mother.father.id
    father = Member.query.filter_by(id=father_id).first()
    if father:
        if father.mother:
            grandmother_by_father_id = father.mother.id
        if father.father:
            grandfather_by_father_id = father.father.id
    new_child_member = Member(role=role, gender=gender, full_name=full_name,
                              date_of_birth=date_of_birth, place_of_birth=place_of_birth,
                              complete_address=complete_address, deceased=deceased,
                              spouse_full_name=spouse_full_name, spouse_date_of_birth=spouse_date_of_birth, spouse_place_of_birth=spouse_place_of_birth,
                              inlaws_full_name=inlaws_full_name, father_inlaws_full_address=father_inlaws_full_address, father_inlaws_deceased=father_inlaws_deceased,
                              mother_id=mother_id, father_id=father_id,
                              grandmother_by_mother_id=grandmother_by_mother_id,
                              grandfather_by_mother_id=grandfather_by_mother_id,
                              grandmother_by_father_id=grandmother_by_father_id,
                              grandfather_by_father_id=grandfather_by_father_id
    )
    db.session.add(new_child_member)
    db.session.commit()
    return new_child_member


def add_grandchild_member(role=None, gender=None, full_name=None,
                          date_of_birth=None, place_of_birth=None,
                          complete_address=None, deceased=None,
                          mother_id=None, father_id=None
    ):
    #
    grandmother_by_mother_id = None
    grandfather_by_mother_id = None
    grandmother_by_father_id = None
    grandfather_by_father_id = None
    #
    grandmother_by_grandmother_by_mother_id = None
    grandfather_by_grandmother_by_mother_id = None
    grandmother_by_grandfather_by_mother_id = None
    grandfather_by_grandfather_by_mother_id = None
    grandmother_by_grandmother_by_father_id = None
    grandfather_by_grandmother_by_father_id = None
    grandmother_by_grandfather_by_father_id = None
    grandfather_by_grandfather_by_father_id = None
    #
    mother = Member.query.filter_by(id=mother_id).first()
    if mother:
        if mother.mother:
            grandmother_by_mother_id = mother.mother.id
            #
            if mother.mother.mother:
                grandmother_by_grandmother_by_mother_id = mother.mother.mother.id
            if mother.mother.father:
                grandfather_by_grandmother_by_mother_id = mother.mother.father.id
        if mother.father:
            grandfather_by_mother_id = mother.father.id
            #
            if mother.father.mother:
                grandmother_by_grandfather_by_mother_id = mother.father.mother.id
            if mother.father.father:
                grandfather_by_grandfather_by_mother_id = mother.father.father.id
    father = Member.query.filter_by(id=father_id).first()
    if father:
        if father.mother:
            grandmother_by_father_id = father.mother.id
            #
            if father.mother.mother:
                grandmother_by_grandmother_by_father_id = father.mother.mother.id
            if father.mother.father:
                grandfather_by_grandmother_by_father_id = father.mother.father.id
        if father.father:
            grandfather_by_father_id = father.father.id
            #
            if father.father.mother:
                grandmother_by_grandfather_by_father_id = father.father.mother.id
            if father.father.father:
                grandfather_by_grandfather_by_father_id = father.father.father.id
    new_child_member = Member(role=role, gender=gender, full_name=full_name,
                              date_of_birth=date_of_birth, place_of_birth=place_of_birth,
                              complete_address=complete_address, deceased=deceased,
                              mother_id=mother_id, father_id=father_id,
                              grandmother_by_mother_id=grandmother_by_mother_id,
                              grandfather_by_mother_id=grandfather_by_mother_id,
                              grandmother_by_father_id=grandmother_by_father_id,
                              grandfather_by_father_id=grandfather_by_father_id,
                              grandmother_by_grandmother_by_mother_id=grandmother_by_grandmother_by_mother_id,
                              grandfather_by_grandmother_by_mother_id=grandfather_by_grandmother_by_mother_id,
                              grandmother_by_grandfather_by_mother_id=grandmother_by_grandfather_by_mother_id,
                              grandfather_by_grandfather_by_mother_id=grandfather_by_grandfather_by_mother_id,
                              grandmother_by_grandmother_by_father_id=grandmother_by_grandmother_by_father_id,
                              grandfather_by_grandmother_by_father_id=grandfather_by_grandmother_by_father_id,
                              grandmother_by_grandfather_by_father_id=grandmother_by_grandfather_by_father_id,
                              grandfather_by_grandfather_by_father_id=grandfather_by_grandfather_by_father_id
                              )
    db.session.add(new_child_member)
    db.session.commit()
    return new_child_member
