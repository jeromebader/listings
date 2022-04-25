import sqlalchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session
from config import Config
from forms import SignupForm
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    uid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(length=64))
    email = sqlalchemy.Column(sqlalchemy.String(length=100))
    password = sqlalchemy.Column(sqlalchemy.String(length=120))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=64))
    roleid = sqlalchemy.Column(sqlalchemy.Integer)
    userstatus = sqlalchemy.Column(sqlalchemy.String)
    usercreation = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    company = sqlalchemy.Column(sqlalchemy.String)
    # approves = sqlalchemy.Column(sqlalchemy.String)


    def __repr__(self):
        return "uid='{0}', username='{1}', email= '{2}', password='{3}', fullname = '{4}', roleid = '{5}', userstatus = '{6}', usercreation='{7}', company='{8}', approves='{9}'".format(self.uid, self.username, self.email, self.password, self.fullname, self.roleid, self.userstatus, self.usercreation, self.company, self.approves)


class Listing(Base):
    __tablename__ = 'listings'

    listing_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    uid = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('users.uid'))
    listing_title = sqlalchemy.Column(sqlalchemy.String(length=50))
    listing_domain = sqlalchemy.Column(sqlalchemy.String(length=50))
    listing_description = sqlalchemy.Column(sqlalchemy.TEXT(length=100))
    listing_price = sqlalchemy.Column(sqlalchemy.DECIMAL(precision=10, scale=2))
    listing_expiration = sqlalchemy.Column(sqlalchemy.Date)
    listing_start = sqlalchemy.Column(sqlalchemy.Date)
    listing_creation = sqlalchemy.Column(sqlalchemy.TIMESTAMP)


    listing_status = sqlalchemy.Column(sqlalchemy.String)
    listing_type = sqlalchemy.Column(sqlalchemy.String)
    listing_special = sqlalchemy.Column(sqlalchemy.String)
    listing_buyer =  sqlalchemy.Column(sqlalchemy.Integer)
    listing_multimedia = sqlalchemy.Column(sqlalchemy.JSON)
    # listing_approver1 = sqlalchemy.Column(sqlalchemy.String)
    # listing_approver2 = sqlalchemy.Column(sqlalchemy.String)
    # listing_approver3 = sqlalchemy.Column(sqlalchemy.String)
    # listing_approver4 = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return "listing_id='{0}', uid='{1}', listing_title='{2}', listing_domain='{3}', listing_description='{4}', listing_price='{5}', listing_expiration ='{6}', listing_start='{7}', listing_creation='{8}', listing_status='{9}', listing_type='{10}', listing_special='{11}'. listing_buyer='{12}', listing_multimedia='{13}' ".format(
            self.listing_id, self.uid, self.listing_title, self.listing_domain, self.listing_description, self.listing_price, self.listing_expiration, self.listing_start, self.listing_creation, self.listing_status, self.listing_type, self.listing_special,self.listing_buyer, self.listing_multimedia)



# class Listing(Base):
#     __tablename__ = 'approvals'
#
#     approval_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#     listing_id =
#     approver1 =
#     approver2 =
#     approver3 =
#     approver4 =
#     approval_status1 = (pending), (yes), (no)
#     approval_status2 =
#     approval_status3 =
#     approval_status4 =
#     approval_time1 = timestamp
#     approval_time2 =
#     approval_time3 =
#     approval_time4 =
#     approval_ip1 = ip of client
#     approval_ip2 =
#     approval_ip3 =
#     approval_ip4 =






#
# class transaction(Base):
#     __tablename__ = 'transaction'








class Role(Base):
    __tablename__ = 'role'

    roleid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    rolename = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return "roleid='{0}', rolename='{1}'".format( self.roleid, self.rolename)