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
    get_user_data           =[]
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

                
        report_active       	=	False
        report_read         	=	False
        report_write        	=	False
        entity_type_active  	=	False
        entity_type_read    	=	False
        entity_type_write   	=	False
        entity_list_active  	=	False
        entity_list_read    	=	False
        entity_list_write   	=	False
        entity_category_active  	=	False
        entity_category_read    	=	False
        entity_category_write   	=	False
        branch_active           	=	False
        branch_read             	=	False
        branch_write            	=	False
        user_role_active        	=	False
        user_role_read          	=	False
        user_role_write         	=	False
        role_permission_active  	=	False
        role_permission_read    	=	False
        role_permission_write   	=	False
        user_list_active        	=	False
        user_list_read          	=	False
        user_list_write         	=	False
        series_active           	=	False
        series_read             	=	False
        series_write            	=	False
        customer_type_active    	=	False
        customer_type_read      	=	False
        customer_type_write     	=	False
        customer_list_active    	=	False
        customer_list_read      	=	False
        customer_list_write     	=	False
        supplier_type_active    	=	False
        supplier_type_read      	=	False
        supplier_type_write     	=	False
        supplier_list_active    	=	False
        supplier_list_read      	=	False
        supplier_list_write     	=	False
        accounting_group_active 	=	False
        accounting_group_read   	=	False
        accounting_group_write  	=	False
        accounting_ledger_active   	=	False
        accounting_ledger_read  	=	False
        accounting_ledger_write 	=	False
        financial_year_active   	=	False
        financial_year_read     	=	False
        financial_year_write    	=	False
        warehouse_active        	=	False
        warehouse_read          	=	False
        warehouse_write         	=	False
        brand_active            	=	False
        brand_read              	=	False
        brand_write             	=	False
        model_number_active     	=	False
        model_number_read       	=	False
        model_number_write      	=	False
        size_active             	=	False
        size_read               	=	False
        size_write              	=	False
        unit_active             	=	False
        unit_read               	=	False
        unit_write              	=	False
        godown_active           	=	False
        godown_read             	=	False
        godown_write            	=	False
        rack_active             	=	False
        rack_write              	=	False
        rack_read               	=	False
        product_group_active    	=	False
        product_group_read      	=	False
        product_group_write     	=	False
        product_active          	=	False
        product_read            	=	False
        product_write           	=	False
        pricing_level_active    	=	False
        pricing_level_read      	=	False
        pricing_level_write     	=	False
        batch_active            	=	False
        batch_read              	=	False
        batch_write             	=	False
        general_active          	=	False
        general_read            	=	False
        general_write           	=	False
        tax_active              	=	False
        tax_read                	=	False
        tax_write               	=	False
        voucher_type_active     	=	False
        voucher_type_read       	=	False
        voucher_type_write      	=	False
        voucher_series_active   	=	False
        voucher_series_read     	=	False
        voucher_series_write    	=	False
        location_active         	=	False
        location_read           	=	False
        location_write          	=	False
        gst_treatment_active    	=	False
        gst_treatment_read      	=	False
        gst_treatment_write     	=	False


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

                        
            report_active       	=	True
            report_read         	=	True
            report_write        	=	True
            entity_type_active  	=	True
            entity_type_read    	=	True
            entity_type_write   	=	True
            entity_list_active  	=	True
            entity_list_read    	=	True
            entity_list_write   	=	True
            entity_category_active  	=	True
            entity_category_read    	=	True
            entity_category_write   	=	True
            branch_active           	=	True
            branch_read             	=	True
            branch_write            	=	True
            user_role_active        	=	True
            user_role_read          	=	True
            user_role_write         	=	True
            role_permission_active  	=	True
            role_permission_read    	=	True
            role_permission_write   	=	True
            user_list_active        	=	True
            user_list_read          	=	True
            user_list_write         	=	True
            series_active           	=	True
            series_read             	=	True
            series_write            	=	True
            customer_type_active    	=	True
            customer_type_read      	=	True
            customer_type_write     	=	True
            customer_list_active    	=	True
            customer_list_read      	=	True
            customer_list_write     	=	True
            supplier_type_active    	=	True
            supplier_type_read      	=	True
            supplier_type_write     	=	True
            supplier_list_active    	=	True
            supplier_list_read      	=	True
            supplier_list_write     	=	True
            accounting_group_active 	=	True
            accounting_group_read   	=	True
            accounting_group_write  	=	True
            accounting_ledger_active   	=	True
            accounting_ledger_read  	=	True
            accounting_ledger_write 	=	True
            financial_year_active   	=	True
            financial_year_read     	=	True
            financial_year_write    	=	True
            warehouse_active        	=	True
            warehouse_read          	=	True
            warehouse_write         	=	True
            brand_active            	=	True
            brand_read              	=	True
            brand_write             	=	True
            model_number_active     	=	True
            model_number_read       	=	True
            model_number_write      	=	True
            size_active             	=	True
            size_read               	=	True
            size_write              	=	True
            unit_active             	=	True
            unit_read               	=	True
            unit_write              	=	True
            godown_active           	=	True
            godown_read             	=	True
            godown_write            	=	True
            rack_active             	=	True
            rack_write              	=	True
            rack_read               	=	True
            product_group_active    	=	True
            product_group_read      	=	True
            product_group_write     	=	True
            product_active          	=	True
            product_read            	=	True
            product_write           	=	True
            pricing_level_active    	=	True
            pricing_level_read      	=	True
            pricing_level_write     	=	True
            batch_active            	=	True
            batch_read              	=	True
            batch_write             	=	True
            general_active          	=	True
            general_read            	=	True
            general_write           	=	True
            tax_active              	=	True
            tax_read                	=	True
            tax_write               	=	True
            voucher_type_active     	=	True
            voucher_type_read       	=	True
            voucher_type_write      	=	True
            voucher_series_active   	=	True
            voucher_series_read     	=	True
            voucher_series_write    	=	True
            location_active         	=	True
            location_read           	=	True
            location_write          	=	True
            gst_treatment_active    	=	True
            gst_treatment_read      	=	True
            gst_treatment_write     	=	True


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
                role_permission         = user_role_permission.objects.filter(user_role_id=get_user_data.user_role_id.id).exists()
                
                if role_permission:
                    role_permission     = user_role_permission.objects.get(user_role_id=get_user_data.user_role_id.id)

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

                                            
                    entity_type_active  	    =	role_permission.entity_type_active  
                    entity_type_read    	    =	role_permission.entity_type_read    
                    entity_type_write   	    =	role_permission.entity_type_write   
                    entity_list_active  	    =	role_permission.entity_list_active  
                    entity_list_read    	    =	role_permission.entity_list_read    
                    entity_list_write   	    =	role_permission.entity_list_write   
                    entity_category_active  	=	role_permission.entity_category_active  
                    entity_category_read    	=	role_permission.entity_category_read    
                    entity_category_write   	=	role_permission.entity_category_write   
                    branch_active           	=	role_permission.branch_active           
                    branch_read             	=	role_permission.branch_read             
                    branch_write            	=	role_permission.branch_write            
                    user_role_active        	=	role_permission.user_role_active        
                    user_role_read          	=	role_permission.user_role_read          
                    user_role_write         	=	role_permission.user_role_write         
                    role_permission_active  	=	role_permission.role_permission_active  
                    role_permission_read    	=	role_permission.role_permission_read    
                    role_permission_write   	=	role_permission.role_permission_write   
                    user_list_active        	=	role_permission.user_list_active        
                    user_list_read          	=	role_permission.user_list_read          
                    user_list_write         	=	role_permission.user_list_write         
                    series_active           	=	role_permission.series_active           
                    series_read             	=	role_permission.series_read             
                    series_write            	=	role_permission.series_write            
                    customer_type_active    	=	role_permission.customer_type_active    
                    customer_type_read      	=	role_permission.customer_type_read      
                    customer_type_write     	=	role_permission.customer_type_write     
                    customer_list_active    	=	role_permission.customer_list_active    
                    customer_list_read      	=	role_permission.customer_list_read      
                    customer_list_write     	=	role_permission.customer_list_write     
                    supplier_type_active    	=	role_permission.supplier_type_active    
                    supplier_type_read      	=	role_permission.supplier_type_read      
                    supplier_type_write     	=	role_permission.supplier_type_write     
                    supplier_list_active    	=	role_permission.supplier_list_active    
                    supplier_list_read      	=	role_permission.supplier_list_read      
                    supplier_list_write     	=	role_permission.supplier_list_write     
                    accounting_group_active 	=	role_permission.accounting_group_active 
                    accounting_group_read   	=	role_permission.accounting_group_read   
                    accounting_group_write  	=	role_permission.accounting_group_write  
                    accounting_ledger_active   	=	role_permission.accounting_ledger_active   
                    accounting_ledger_read  	=	role_permission.accounting_ledger_read  
                    accounting_ledger_write 	=	role_permission.accounting_ledger_write 
                    financial_year_active   	=	role_permission.financial_year_active   
                    financial_year_read     	=	role_permission.financial_year_read     
                    financial_year_write    	=	role_permission.financial_year_write    
                    warehouse_active        	=	role_permission.warehouse_active        
                    warehouse_read          	=	role_permission.warehouse_read          
                    warehouse_write         	=	role_permission.warehouse_write         
                    brand_active            	=	role_permission.brand_active            
                    brand_read              	=	role_permission.brand_read              
                    brand_write             	=	role_permission.brand_write             
                    model_number_active     	=	role_permission.model_number_active     
                    model_number_read       	=	role_permission.model_number_read       
                    model_number_write      	=	role_permission.model_number_write      
                    size_active             	=	role_permission.size_active             
                    size_read               	=	role_permission.size_read               
                    size_write              	=	role_permission.size_write              
                    unit_active             	=	role_permission.unit_active             
                    unit_read               	=	role_permission.unit_read               
                    unit_write              	=	role_permission.unit_write              
                    godown_active           	=	role_permission.godown_active           
                    godown_read             	=	role_permission.godown_read             
                    godown_write            	=	role_permission.godown_write            
                    rack_active             	=	role_permission.rack_active             
                    rack_write              	=	role_permission.rack_write              
                    rack_read               	=	role_permission.rack_read               
                    product_group_active    	=	role_permission.product_group_active    
                    product_group_read      	=	role_permission.product_group_read      
                    product_group_write     	=	role_permission.product_group_write     
                    product_active          	=	role_permission.product_active          
                    product_read            	=	role_permission.product_read            
                    product_write           	=	role_permission.product_write           
                    pricing_level_active    	=	role_permission.pricing_level_active    
                    pricing_level_read      	=	role_permission.pricing_level_read      
                    pricing_level_write     	=	role_permission.pricing_level_write     
                    batch_active            	=	role_permission.batch_active            
                    batch_read              	=	role_permission.batch_read              
                    batch_write             	=	role_permission.batch_write             
                    general_active          	=	role_permission.general_active          
                    general_read            	=	role_permission.general_read            
                    general_write           	=	role_permission.general_write           
                    tax_active              	=	role_permission.tax_active              
                    tax_read                	=	role_permission.tax_read                
                    tax_write               	=	role_permission.tax_write               
                    voucher_type_active     	=	role_permission.voucher_type_active     
                    voucher_type_read       	=	role_permission.voucher_type_read       
                    voucher_type_write      	=	role_permission.voucher_type_write      
                    voucher_series_active   	=	role_permission.voucher_series_active   
                    voucher_series_read     	=	role_permission.voucher_series_read     
                    voucher_series_write    	=	role_permission.voucher_series_write    
                    location_active         	=	role_permission.location_active         
                    location_read           	=	role_permission.location_read           
                    location_write          	=	role_permission.location_write          
                    gst_treatment_active    	=	role_permission.gst_treatment_active    
                    gst_treatment_read      	=	role_permission.gst_treatment_read      
                    gst_treatment_write     	=	role_permission.gst_treatment_write     
                    report_active           	=	role_permission.report_active           
                    report_read             	=	role_permission.report_read             
                    report_write            	=	role_permission.report_write            




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

                                                                                            
                                            'entity_type_active'  	    :	entity_type_active              ,
                                            'entity_type_read'    	    :	entity_type_read    ,
                                            'entity_type_write'   	    :	entity_type_write   ,
                                            'entity_list_active'  	    :	entity_list_active  ,
                                            'entity_list_read'    	    :	entity_list_read    ,
                                            'entity_list_write'   	    :	entity_list_write   ,
                                            'entity_category_active'  	:	entity_category_active  ,
                                            'entity_category_read'    	:	entity_category_read    ,
                                            'entity_category_write'   	:	entity_category_write   ,
                                            'branch_active'           	:	branch_active           ,
                                            'branch_read'             	:	branch_read             ,
                                            'branch_write'            	:	branch_write            ,
                                            'user_role_active'        	:	user_role_active        ,
                                            'user_role_read'          	:	user_role_read          ,
                                            'user_role_write'         	:	user_role_write         ,
                                            'role_permission_active'  	:	role_permission_active  ,
                                            'role_permission_read'    	:	role_permission_read    ,
                                            'role_permission_write'   	:	role_permission_write   ,
                                            'user_list_active'        	:	user_list_active        ,
                                            'user_list_read'          	:	user_list_read          ,
                                            'user_list_write'         	:	user_list_write         ,
                                            'series_active'           	:	series_active           ,
                                            'series_read'             	:	series_read             ,
                                            'series_write'            	:	series_write            ,
                                            'customer_type_active'    	:	customer_type_active    ,
                                            'customer_type_read'      	:	customer_type_read      ,
                                            'customer_type_write'     	:	customer_type_write     ,
                                            'customer_list_active'    	:	customer_list_active    ,
                                            'customer_list_read'      	:	customer_list_read      ,
                                            'customer_list_write'     	:	customer_list_write     ,
                                            'supplier_type_active'    	:	supplier_type_active    ,
                                            'supplier_type_read'      	:	supplier_type_read      ,
                                            'supplier_type_write'     	:	supplier_type_write     ,
                                            'supplier_list_active'    	:	supplier_list_active    ,
                                            'supplier_list_read'      	:	supplier_list_read      ,
                                            'supplier_list_write'     	:	supplier_list_write     ,
                                            'accounting_group_active' 	:	accounting_group_active ,
                                            'accounting_group_read'   	:	accounting_group_read   ,
                                            'accounting_group_write'  	:	accounting_group_write  ,
                                            'accounting_ledger_active'   	:	accounting_ledger_active   ,
                                            'accounting_ledger_read'  	:	accounting_ledger_read  ,
                                            'accounting_ledger_write' 	:	accounting_ledger_write ,
                                            'financial_year_active'   	:	financial_year_active   ,
                                            'financial_year_read'     	:	financial_year_read     ,
                                            'financial_year_write'    	:	financial_year_write    ,
                                            'warehouse_active'        	:	warehouse_active        ,
                                            'warehouse_read'          	:	warehouse_read          ,
                                            'warehouse_write'         	:	warehouse_write         ,
                                            'brand_active'            	:	brand_active            ,
                                            'brand_read'              	:	brand_read              ,
                                            'brand_write'             	:	brand_write             ,
                                            'model_number_active'     	:	model_number_active     ,
                                            'model_number_read'       	:	model_number_read       ,
                                            'model_number_write'      	:	model_number_write      ,
                                            'size_active'             	:	size_active             ,
                                            'size_read'               	:	size_read               ,
                                            'size_write'              	:	size_write              ,
                                            'unit_active'             	:	unit_active             ,
                                            'unit_read'               	:	unit_read               ,
                                            'unit_write'              	:	unit_write              ,
                                            'godown_active'           	:	godown_active           ,
                                            'godown_read'             	:	godown_read             ,
                                            'godown_write'            	:	godown_write            ,
                                            'rack_active'             	:	rack_active             ,
                                            'rack_write'              	:	rack_write              ,
                                            'rack_read'               	:	rack_read               ,
                                            'product_group_active'    	:	product_group_active    ,
                                            'product_group_read'      	:	product_group_read      ,
                                            'product_group_write'     	:	product_group_write     ,
                                            'product_active'          	:	product_active          ,
                                            'product_read'            	:	product_read            ,
                                            'product_write'           	:	product_write           ,
                                            'pricing_level_active'    	:	pricing_level_active    ,
                                            'pricing_level_read'      	:	pricing_level_read      ,
                                            'pricing_level_write'     	:	pricing_level_write     ,
                                            'batch_active'            	:	batch_active            ,
                                            'batch_read'              	:	batch_read              ,
                                            'batch_write'             	:	batch_write             ,
                                            'general_active'          	:	general_active          ,
                                            'general_read'            	:	general_read            ,
                                            'general_write'           	:	general_write           ,
                                            'tax_active'              	:	tax_active              ,
                                            'tax_read'                	:	tax_read                ,
                                            'tax_write'               	:	tax_write               ,
                                            'voucher_type_active'     	:	voucher_type_active     ,
                                            'voucher_type_read'       	:	voucher_type_read       ,
                                            'voucher_type_write'      	:	voucher_type_write      ,
                                            'voucher_series_active'   	:	voucher_series_active   ,
                                            'voucher_series_read'     	:	voucher_series_read     ,
                                            'voucher_series_write'    	:	voucher_series_write    ,
                                            'location_active'         	:	location_active         ,
                                            'location_read'           	:	location_read           ,
                                            'location_write'          	:	location_write          ,
                                            'gst_treatment_active'    	:	gst_treatment_active    ,
                                            'gst_treatment_read'      	:	gst_treatment_read      ,
                                            'gst_treatment_write'     	:	gst_treatment_write     ,
                                            'report_active'           	:	report_active           ,
                                            'report_read'             	:	report_read             ,
                                            'report_write'            	:	report_write            ,
                       
                                        }
    
    return {'all_user_role_permission': all_user_role_permission,'get_user_data':get_user_data}