'''
Created on Jan 14, 2018

@author: Admin
'''
import decimal, datetime

class Serializer(object):
    '''
    classdocs
    '''


    __public__ = None

    def to_serializable_dict(self):
        dict = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            if value:
                dict[public_key] = value
        return dict
    
    def alchemyencoder(self):
        """JSON encoder function for SQLAlchemy special classes."""
        if isinstance(self, datetime.date):
            return self.isoformat()
        elif isinstance(self, decimal.Decimal):
            return float(self)
        
        
    def to_dict(self,model_instance, query_instance=None):
        if hasattr(model_instance, '__table__'):
            return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
        else:
             cols = query_instance.column_descriptions
             return { cols[i]['name'] : model_instance[i]  for i in range(len(cols)) }