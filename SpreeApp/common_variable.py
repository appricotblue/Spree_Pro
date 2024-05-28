from datetime import datetime
from .models import *

def getCommonData(request): 
    common_user_data        = {}
    all_entities            = []
    
    if request.session.has_key('userId'):
        print(request.session.get('userId'))
        print("############")
        user_id             = request.session.get('userId')
        common_user_data    = user_data.objects.filter(id=user_id)
        if common_user_data:
            common_user_data    = user_data.objects.get(id=user_id)
            list_entity         = entity_data.objects.all()
            all_entities        = []
            user_entity         = common_user_data.entity_id
            if user_entity:
                user_entities   = common_user_data.entity_id.split(',')
                print(user_entities)
                list_entity = list_entity.filter(pk__in=user_entities)
                print(list_entity)
                
            for entity in list_entity:
                    selected        = ''
                    if common_user_data.default_entity_id:
                        if int(common_user_data.default_entity_id.id) == int(entity.id):
                            selected    = 'selected'
                        
                    all_entities.append({
                        'id'        : entity.id,
                        'name'      : entity.name,
                        'selected'  : selected
                    })
                

                    



    return {'common_user_data':common_user_data,'common_entities':all_entities}       



def getUserPermissions(request):
    all_user_role_permission= []
    if request.session.has_key('userId'):
        user_id             = request.session.get('userId')
        get_user_data       = user_data.objects.get(id=user_id)
        get_added_user      = get_user_data.added_by

        entity_active       = False 
        entity_read         = False
        entity_write        = False  

        users_active        = False
        users_read          = False
        users_write         = False
        
        customer_active     = False
        customers_read      = False
        customers_write     = False
        
        supplier_active     = False
        supplier_read       = False
        supplier_write      = False

        accounting_active   = False
        accounting_read     = False
        accounting_write    = False

        invendory_active    = False
        invendory_read      = False
        invendory_write     = False

        general_active      = False
        general_read        = False
        general_write       = False

        purchase_active     = False
        purchase_read       = False
        purchase_write      = False

        sales_active        = False
        sales_read          = False
        sales_write         = False

        transactions_active = False
        transactions_read   = False
        transactions_write  = False

        if not get_user_data.user_role_id: ###super admin
            entity_active       = True
            entity_read         = True
            entity_write        = True
            
            users_active        = True
            users_read          = True
            users_write         = True
            
            customer_active     = True
            customers_read      = True
            customers_write     = True
            
            supplier_active     = True
            supplier_read       = True
            supplier_write      = True

            accounting_active   = True
            accounting_read     = True 
            accounting_write    = True 

            invendory_active    = True 
            invendory_read      = True 
            invendory_write     = True 

            general_active      = True
            general_read        = True 
            general_write       = True 

            purchase_active     = True 
            purchase_read       = True 
            purchase_write      = True 

            sales_active        = True 
            sales_read          = True 
            sales_write         = True 

            transactions_active = True 
            transactions_read   = True 
            transactions_write  = True 
        else:
            # if get_added_user.id:
            #     role_permission         = user_role_permission.objects.filter(user_id=get_added_user.id,user_role_id=get_user_data.user_role_id.id).exists();
                
            #     if role_permission:
            #         role_permission     = user_role_permission.objects.get(user_id=get_added_user.id,user_role_id=get_user_data.user_role_id.id)

            #         entity_active       = role_permission.entity_active
            #         entity_read         = role_permission.entity_read
            #         entity_write        = role_permission.entity_write

            #         users_active        = role_permission.users_active
            #         users_read          = role_permission.users_read
            #         users_write         = role_permission.users_write
                    
            #         customer_active     = role_permission.customer_active
            #         customers_read      = role_permission.customers_read
            #         customers_write     = role_permission.customers_write
                    
            #         supplier_active     = role_permission.supplier_active
            #         supplier_read       = role_permission.supplier_read
            #         supplier_write      = role_permission.supplier_write

            #         accounting_active   = role_permission.accounting_active
            #         accounting_read     = role_permission.accounting_read 
            #         accounting_write    = role_permission.accounting_write 

            #         invendory_active    = role_permission.invendory_active 
            #         invendory_read      = role_permission.invendory_read 
            #         invendory_write     = role_permission.invendory_write 

            #         general_active      = role_permission.general_active 
            #         general_read        = role_permission.general_read  
            #         general_write       = role_permission.general_write  

            #         purchase_active     = role_permission.purchase_active  
            #         purchase_read       = role_permission.purchase_read  
            #         purchase_write      = role_permission.purchase_write  

            #         sales_active        = role_permission.sales_active  
            #         sales_read          = role_permission.sales_read  
            #         sales_write         = role_permission.sales_write  

            #         transactions_active = role_permission.transactions_active  
            #         transactions_read   = role_permission.transactions_read  
            #         transactions_write  = role_permission.transactions_write  
            # else:
                role_permission         = user_role_permission.objects.filter(user_id=get_user_data.id,user_role_id=get_user_data.user_role_id.id).exists()
                
                if role_permission:
                    role_permission     = user_role_permission.objects.get(pk=1)

                    entity_active       = role_permission.entity_active
                    entity_read         = role_permission.entity_read
                    entity_write        = role_permission.entity_write

                    users_active        = role_permission.users_active
                    users_read          = role_permission.users_read
                    users_write         = role_permission.users_write
                    
                    customer_active     = role_permission.customer_active
                    customers_read      = role_permission.customers_read
                    customers_write     = role_permission.customers_write
                    
                    supplier_active     = role_permission.supplier_active
                    supplier_read       = role_permission.supplier_read
                    supplier_write      = role_permission.supplier_write

                    accounting_active   = role_permission.accounting_active
                    accounting_read     = role_permission.accounting_read 
                    accounting_write    = role_permission.accounting_write 

                    invendory_active    = role_permission.invendory_active 
                    invendory_read      = role_permission.invendory_read 
                    invendory_write     = role_permission.invendory_write 

                    general_active      = role_permission.general_active 
                    general_read        = role_permission.general_read  
                    general_write       = role_permission.general_write  

                    purchase_active     = role_permission.purchase_active  
                    purchase_read       = role_permission.purchase_read  
                    purchase_write      = role_permission.purchase_write  

                    sales_active        = role_permission.sales_active  
                    sales_read          = role_permission.sales_read  
                    sales_write         = role_permission.sales_write  

                    transactions_active = role_permission.transactions_active  
                    transactions_read   = role_permission.transactions_read  
                    transactions_write  = role_permission.transactions_write  

        all_user_role_permission        =   {
                                            'entity_active'         : entity_active,
                                            'entity_read'           : entity_read,
                                            'entity_write'          : entity_write,

                                            'users_active'          : users_active,
                                            'users_read'            : users_read,
                                            'users_write'           : users_write,
                                            
                                            'customer_active'       : customer_active,
                                            'customers_read'        : customers_read,
                                            'customers_write'       : customers_write,
                                            
                                            'supplier_active'       : supplier_active,
                                            'supplier_read'         : supplier_read,
                                            'supplier_write'        : supplier_write,

                                            'accounting_active'     : accounting_active,
                                            'accounting_read'       : accounting_read,
                                            'accounting_write'      : accounting_write, 

                                            'invendory_active'      : invendory_active, 
                                            'invendory_read'        : invendory_read, 
                                            'invendory_write'       : invendory_write, 

                                            'general_active'        : general_active, 
                                            'general_read'          : general_read,  
                                            'general_write'         : general_write,  

                                            'purchase_active'       : purchase_active,  
                                            'purchase_read'         : purchase_read,  
                                            'purchase_write'        : purchase_write,  

                                            'sales_active'          : sales_active,  
                                            'sales_read'            : sales_read,  
                                            'sales_write'           : sales_write,  

                                            'transactions_active'   : transactions_active,  
                                            'transactions_read'     : transactions_read,  
                                            'transactions_write'    : transactions_write,  
                                        }

    
    return {'all_user_role_permission': all_user_role_permission}