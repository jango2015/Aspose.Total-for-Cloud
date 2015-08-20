#!/usr/bin/env python

class StorageExistResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'IsExist': 'bool',
            'Code': 'str',
            'Status': 'str'

        }

        self.attributeMap = {
            'IsExist': 'IsExist','Code': 'Code','Status': 'Status'}       

        self.IsExist = None # bool
        self.Code = None # str
        self.Status = None # str
        
