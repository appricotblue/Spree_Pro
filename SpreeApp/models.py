from django.db import models
from django.utils import timezone

# Create your models here.

class entity_type(models.Model):
    type            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class entity_category(models.Model):
    category        = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')




class location_data(models.Model):
    location        = models.CharField(max_length=100,default='')
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class gst_treatment_data(models.Model):
    name            = models.TextField()
    description     = models.TextField(default='',null=True)



class entity_data(models.Model):
    name            = models.CharField(max_length=100,default='')
    entity_type_id  = models.ForeignKey(entity_type,on_delete=models.CASCADE,default='',null=True)
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    location        = models.ForeignKey(location_data,on_delete=models.SET_NULL,null=True)
    updated_at      = models.DateTimeField(max_length=100,default='')


class branch_data(models.Model):
    entity_id       = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    name            = models.CharField(max_length=100,default='',null=True)
    branch_code     = models.CharField(max_length=100,default='',null=True)
    address         = models.CharField(max_length=100,default='',null=True)
    city            = models.CharField(max_length=100,default='',null=True)
    state           = models.CharField(max_length=100,default='32',null=True)
    country         = models.CharField(max_length=100,default='',null=True)
    pincode         = models.CharField(max_length=100,default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')
    gst_treatment       = models.ForeignKey(gst_treatment_data,on_delete=models.SET_NULL,null=True)


class user_roles(models.Model):
    role            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    client_access       = models.BooleanField(max_length=100,default=0)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class user_data(models.Model):
    branch_id           = models.TextField(default='',null=True)
    user_role_id        = models.ForeignKey(user_roles,on_delete=models.CASCADE,default='',null=True)
    entity_id           = models.TextField(default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    email               = models.CharField(max_length=100,default='',null=True)
    password            = models.CharField(max_length=100,default='',null=True)
    profile_image       = models.ImageField(upload_to='image',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    added_by            = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='accound_group')
    default_entity_id   = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class user_role_permission(models.Model):
    user_id             = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True)
    user_role_id        = models.ForeignKey(user_roles,on_delete=models.CASCADE,default='',null=True)
    description         = models.TextField(default='',null=True)
    client_access       = models.BooleanField(max_length=100,default=0)
    entity_active       = models.BooleanField(max_length=100,default=0)
    entity_read         = models.BooleanField(max_length=100,default=0)
    entity_write        = models.BooleanField(max_length=100,default=0)
    users_active        = models.BooleanField(max_length=100,default=0)
    users_read          = models.BooleanField(max_length=100,default=0)
    users_write         = models.BooleanField(max_length=100,default=0)
    customer_active     = models.BooleanField(max_length=100,default=0)
    customers_read      = models.BooleanField(max_length=100,default=0)
    customers_write     = models.BooleanField(max_length=100,default=0)
    supplier_active     = models.BooleanField(max_length=100,default=0)
    supplier_read       = models.BooleanField(max_length=100,default=0)
    supplier_write      = models.BooleanField(max_length=100,default=0)
    accounting_active   = models.BooleanField(max_length=100,default=0)
    accounting_read     = models.BooleanField(max_length=100,default=0)
    accounting_write    = models.BooleanField(max_length=100,default=0)
    invendory_active    = models.BooleanField(max_length=100,default=0)
    invendory_read      = models.BooleanField(max_length=100,default=0)
    invendory_write     = models.BooleanField(max_length=100,default=0)
    general_active      = models.BooleanField(max_length=100,default=0)
    general_read        = models.BooleanField(max_length=100,default=0)
    general_write       = models.BooleanField(max_length=100,default=0)
    purchase_active     = models.BooleanField(max_length=100,default=0)
    purchase_read       = models.BooleanField(max_length=100,default=0)
    purchase_write      = models.BooleanField(max_length=100,default=0)
    sales_active        = models.BooleanField(max_length=100,default=0)
    sales_read          = models.BooleanField(max_length=100,default=0)
    sales_write         = models.BooleanField(max_length=100,default=0)
    transactions_active = models.BooleanField(max_length=100,default=0)
    transactions_read   = models.BooleanField(max_length=100,default=0)
    transactions_write  = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class accounting_group_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    under_group         = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='accound_group')
    nature              = models.CharField(max_length=100,default='',null=True)
    affect_gross_profit = models.CharField(max_length=100,default='',null=True)
    is_default          = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    



class financial_year_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    from_date           = models.CharField(max_length=100,default='',null=True)
    to_date             = models.TextField(default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class series_data(models.Model):
    type                = models.CharField(max_length=100,default='',null=True)
    pre_text            = models.CharField(max_length=100,default='',null=True)
    post_text           = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class customer_type(models.Model):
    type            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')




class customer_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    customer_type_id    = models.ForeignKey(customer_type,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    phone               = models.CharField(max_length=100,default='',null=True)
    email               = models.CharField(max_length=100,default='',null=True)
    customer_code       = models.CharField(max_length=100,default='',null=True)
    location_id         = models.ForeignKey(location_data,on_delete=models.CASCADE,default='',null=True)
    opening_balance     = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    bill_by_bill        = models.CharField(max_length=100,default='',null=True)
    credit_period       = models.CharField(max_length=100,default='',null=True)
    credit_limit        = models.CharField(max_length=100,default='',null=True)
    address             = models.CharField(max_length=100,default='',null=True)
    city                = models.CharField(max_length=100,default='',null=True)
    state               = models.CharField(max_length=100,default='',null=True)
    country             = models.CharField(max_length=100,default='',null=True)
    pincode             = models.CharField(max_length=100,default='',null=True)
    account_number      = models.CharField(max_length=100,default='',null=True)
    branch_name         = models.CharField(max_length=100,default='',null=True)
    branch_code         = models.CharField(max_length=100,default='',null=True)
    cin                 = models.CharField(max_length=100,default='',null=True)
    pan                 = models.CharField(max_length=100,default='',null=True)
    gst                 = models.CharField(max_length=100,default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)   
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    # additional
    state_code          = models.CharField(max_length=100,default='32',null=True)
    gst_treatment       = models.ForeignKey(gst_treatment_data,on_delete=models.SET_NULL,null=True)

    

class supplier_type(models.Model):
    type            = models.CharField(max_length=100,default='')
    description     = models.TextField(default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class supplier_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    supplier_type_id    = models.ForeignKey(supplier_type,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    phone               = models.CharField(max_length=100,default='',null=True)
    email               = models.CharField(max_length=100,default='',null=True)
    supplier_code       = models.CharField(max_length=100,default='',null=True)
    opening_balance     = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    bill_by_bill        = models.CharField(max_length=100,default='',null=True)
    credit_period       = models.CharField(max_length=100,default='',null=True)
    credit_limit        = models.CharField(max_length=100,default='',null=True)
    address             = models.CharField(max_length=100,default='',null=True)
    city                = models.CharField(max_length=100,default='',null=True)
    state               = models.CharField(max_length=100,default='',null=True)
    country             = models.CharField(max_length=100,default='',null=True)
    pincode             = models.CharField(max_length=100,default='',null=True)
    account_number      = models.CharField(max_length=100,default='',null=True)
    branch_name         = models.CharField(max_length=100,default='',null=True)
    branch_code         = models.CharField(max_length=100,default='',null=True)
    tin                 = models.CharField(max_length=100,default='',null=True)
    pan                 = models.CharField(max_length=100,default='',null=True)
    cst                 = models.CharField(max_length=100,default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    # additional
    state_code          = models.CharField(max_length=100,default='32',null=True)
    gst_treatment       = models.ForeignKey(gst_treatment_data,on_delete=models.SET_NULL,null=True)





class pricing_level_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    percentage          = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class accounting_ledger_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    accounting_group_id = models.ForeignKey(accounting_group_data,on_delete=models.CASCADE,default='',null=True)
    opening_balance     = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    bill_by_bill        = models.CharField(max_length=100,default='',null=True)
    supplier_id         = models.ForeignKey(supplier_data,on_delete=models.CASCADE,default='',null=True)
    is_default          = models.BooleanField(max_length=100,default=0)
    customer_id         = models.ForeignKey(customer_data,on_delete=models.CASCADE,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    credit_period       = models.CharField(max_length=100,default='',null=True)
    credit_limit        = models.CharField(max_length=100,default='',null=True)
    pricing_level       = models.ForeignKey(pricing_level_data,on_delete=models.SET_NULL,null=True)
    additional_expense  = models.BooleanField(max_length=100,default=0)




class unit_data(models.Model):
    unit                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    formal_name         = models.CharField(max_length=100,default='',null=True)
    no_of_decimal_place = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class size_data(models.Model):
    size                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class brand_data(models.Model):
    name                = models.CharField(max_length=100,default='',null=True)
    manufacture         = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class model_number_data(models.Model):
    model_number        = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class godown_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class rack_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    godown_id           = models.ForeignKey(godown_data,on_delete=models.CASCADE,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class product_group_data(models.Model):
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    under_group         = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='product_group')
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class tax_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    tax                 = models.CharField(max_length=100,default='',null=True)
    rate_perc           = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    cgst                = models.CharField(max_length=100,default='',null=True)
    sgst                = models.CharField(max_length=100,default='',null=True)
    igst                = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class warehouse_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    name            = models.CharField(max_length=100,default='',null=True)
    branch_id       = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    address         = models.CharField(max_length=100,default='',null=True)
    city            = models.CharField(max_length=100,default='',null=True)
    state           = models.CharField(max_length=100,default='',null=True)
    country         = models.CharField(max_length=100,default='',null=True)
    pincode         = models.CharField(max_length=100,default='',null=True)
    created_at      = models.DateTimeField(max_length=100,default='')
    updated_at      = models.DateTimeField(max_length=100,default='')


class product_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    warehouse_id        = models.ForeignKey(warehouse_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    product_code        = models.CharField(max_length=100,default='',null=True)
    product_group_id    = models.ForeignKey(product_group_data,on_delete=models.CASCADE,default='',null=True)
    brand_id            = models.ForeignKey(brand_data,on_delete=models.CASCADE,default='',null=True)
    unit_id             = models.ForeignKey(unit_data,on_delete=models.CASCADE,default='',null=True)
    size_id             = models.ForeignKey(size_data,on_delete=models.CASCADE,default='',null=True)
    model_number_id     = models.ForeignKey(model_number_data,on_delete=models.CASCADE,default='',null=True)
    godown_id           = models.TextField(default='',null=True)
    rack_id             = models.TextField(default='',null=True)
    purchase_rate       = models.CharField(max_length=100,default='',null=True)
    mrp                 = models.CharField(max_length=100,default='',null=True)
    sales_rate          = models.CharField(max_length=100,default='',null=True)
    reorder_level       = models.CharField(max_length=100,default=0,null=True)
    minimum_stock       = models.CharField(max_length=100,default=0,null=True)
    maximum_stock       = models.CharField(max_length=100,default='',null=True)
    tax_id              = models.ForeignKey(tax_data,on_delete=models.CASCADE,default='',null=True)
    bom                 = models.CharField(max_length=100,default='',null=True)
    bar_code            = models.CharField(max_length=100,default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    discount_type       = models.CharField(max_length=100,default='',null=True)
    discount            = models.CharField(max_length=100,default='',null=True) 
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    # additional
    product_type        = models.CharField(max_length=100,default='Goods or Service')
    hsn                 = models.CharField(max_length=100,default='')
    sac                 = models.CharField(max_length=100,default='')
    discount_value      = models.CharField(max_length=100,default='')


class batch_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    product_id          = models.ForeignKey(product_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    manufacture_date    = models.CharField(max_length=100,default='',null=True)
    expiry_date         = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    active              = models.BooleanField(max_length=100,default=0)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class voucher_type_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    type_of_voucher     = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='voucher_type')
    start_index         = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class voucher_series_data(models.Model):
    voucher_type_id     = models.ForeignKey(voucher_type_data,on_delete=models.CASCADE,default='',null=True)
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    financial_year_id   = models.ForeignKey(financial_year_data,on_delete=models.CASCADE,default='',null=True)
    name                = models.CharField(max_length=100,default='',null=True)
    prefix              = models.CharField(max_length=100,default='',null=True)
    postfix             = models.CharField(max_length=100,default='',null=True)
    starting_number     = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class voucher_number_data(models.Model):
    voucher_type_id     = models.ForeignKey(voucher_type_data,on_delete=models.CASCADE,default='',null=True)
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    voucher_series_id   = models.ForeignKey(voucher_series_data,on_delete=models.CASCADE,default='',null=True)
    voucher_number      = models.CharField(max_length=100,default='',null=True)
    financial_year_id   = models.ForeignKey(financial_year_data,on_delete=models.CASCADE,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class order_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    user_id             = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    voucher_type_id     = models.ForeignKey(voucher_series_data,on_delete=models.CASCADE,default='',null=True) ##voucher series
    order_number        = models.CharField(max_length=100,default='',null=True) ###voucher_number
    exchange_rate       = models.CharField(max_length=100,default='',null=True)
    date                = models.CharField(max_length=100,default='',null=True)
    due_date            = models.CharField(max_length=100,default='',null=True)
    due_days            = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    total_amount        = models.CharField(max_length=100,default='',null=True)
    generate_invoice    = models.BooleanField(max_length=100,default=0)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    # additional fields
    ewaybill            = models.CharField(max_length=100,default='',null=True)
    transportid         = models.CharField(max_length=100,default='',null=True)
    vehicle_number      = models.CharField(max_length=100,default='',null=True)
    lrno                = models.CharField(max_length=100,default='',null=True)
    no_of_cases         = models.CharField(max_length=100,default='',null=True)
    weight              = models.CharField(max_length=100,default='',null=True)
    pricing_lvl         = models.ForeignKey(pricing_level_data,on_delete=models.CASCADE,default='',null=True)
    shipping_address    = models.TextField(default='',null=True)
    receiver_address   = models.TextField(default='',null=True)
    status                      = models.CharField(max_length=100,default='Pending',null=True)
        # additional
    discount_value              = models.TextField(default='',null=True)
    customer_type_id            = models.ForeignKey(customer_type,on_delete=models.SET_NULL,null=True)
    lut                         = models.TextField(default='',null=True)
    reverse_tax                 = models.TextField(default='',null=True)
    reverse_tax_value           = models.TextField(default='',null=True)
    reverse_cgst                = models.TextField(default='',null=True)
    reverse_sgst                = models.TextField(default='',null=True)
    reverse_igst                = models.TextField(default='',null=True)
    edited_by                   = models.ForeignKey(user_data,on_delete=models.SET_NULL,null=True,related_name="edited_orders")






from django.utils import timezone


class invoice_data(models.Model): ###--- All transactions 
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    user_id             = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True)
    order_id            = models.ForeignKey(order_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    voucher_type_id     = models.ForeignKey(voucher_type_data,on_delete=models.CASCADE,default='',null=True)
    voucher_series_id   = models.ForeignKey(voucher_series_data,on_delete=models.CASCADE,default='',null=True)
    financial_year_id   = models.ForeignKey(financial_year_data,on_delete=models.CASCADE,default='',null=True)
    voucher_number_id   = models.ForeignKey(voucher_number_data,on_delete=models.CASCADE,default='',null=True)
    exchange_rate       = models.CharField(max_length=100,default='',null=True)
    date                = models.CharField(max_length=100,default='',null=True)
    due_date            = models.CharField(max_length=100,default='',null=True)
    due_days            = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    total_amount        = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    invoice_id          = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='edit_invoice') ##Transaction
    debit_ledger_id     = models.ForeignKey(accounting_ledger_data,on_delete=models.CASCADE,default='',null=True, related_name='invoice_debit_ledger_id')
    credit_ledger_id    = models.ForeignKey(accounting_ledger_data,on_delete=models.CASCADE,default='',null=True, related_name='invoice_credit_ledger_id')
    created_by          = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True, related_name='created_by')
    approved_by         = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True, related_name='approved_by')
    status              = models.CharField(max_length=100,default='Pending',null=True)
    against             = models.CharField(max_length=100,default='',null=True)
    cheque_number       = models.CharField(max_length=100,default='',null=True)
    cheque_date         = models.CharField(max_length=100,default='',null=True)
    cgst                = models.CharField(max_length=100,default='',null=True)
    sgst                = models.CharField(max_length=100,default='',null=True)
    igst                = models.CharField(max_length=100,default='',null=True)
    pretax_amount       = models.CharField(max_length=100,default='',null=True)
    
    expence             = models.CharField(max_length=100,default='',null=True)
    ses                 = models.CharField(max_length=100,default='',null=True)
    mrp                 = models.CharField(max_length=100,default='',null=True)
    roundoff            = models.CharField(max_length=100,default='',null=True)
    discount_type       = models.CharField(max_length=100,default='',null=True)
    discount            = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    # additional fields
    ewaybill            = models.CharField(max_length=100,default='',null=True)
    transportid         = models.CharField(max_length=100,default='',null=True)
    vehicle_number      = models.CharField(max_length=100,default='',null=True)
    # lrno                = models.CharField(max_length=100,default='',null=True)
    no_of_cases         = models.CharField(max_length=100,default='',null=True)
    # weight              = models.CharField(max_length=100,default='',null=True)
    pricing_lvl         = models.ForeignKey(pricing_level_data,on_delete=models.CASCADE,default='',null=True)
    transaction_type    = models.CharField(max_length=100,default='',null=True)
    latest              = models.BooleanField(max_length=100,default=0)
    shipping_address    = models.TextField(default='',null=True)
    receiver_address    = models.TextField(default='',null=True)
    # additional
    discount_value              = models.TextField(default='',null=True)
    customer_type_id            = models.ForeignKey(customer_type,on_delete=models.SET_NULL,null=True)
    lut                         = models.TextField(default='',null=True)
    reverse_tax                 = models.TextField(default='',null=True)
    reverse_tax_value           = models.TextField(default='',null=True)
    reverse_cgst                = models.TextField(default='',null=True)
    reverse_sgst                = models.TextField(default='',null=True)
    reverse_igst                = models.TextField(default='',null=True)
    edited_by                   = models.ForeignKey(user_data,on_delete=models.SET_NULL,null=True,related_name="edited_invoice")
    against_po                  = models.ForeignKey(order_data,on_delete=models.CASCADE,null=True,related_name="order_pi")
    against_so                  = models.ForeignKey(order_data,on_delete=models.CASCADE,null=True,related_name="order_si")
    against_sale_quotation      = models.TextField(default='',null=True)
    against_profoma_invoice     = models.TextField(default='',null=True)
    against_credit_note         = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name="debit_note")
    against_debit_note          = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name="credit_note")
    ewaybill_number             = models.CharField(max_length=100,default='',null=True)
    transporter_id              = models.CharField(max_length=100,default='',null=True)
    vehicle_number              = models.CharField(max_length=100,default='',null=True)
    lrno                        = models.CharField(max_length=100,default='',null=True)
    number_of_cases             = models.CharField(max_length=100,default='',null=True)
    weight                      = models.CharField(max_length=100,default='',null=True)
    is_parent                   = models.BooleanField(max_length=100,default=0)
    is_child                    = models.BooleanField(max_length=100,default=0)
    parent_id                   = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='parant_id')
    manuel_invoice_number       =models.CharField(max_length=100,default='',null=True)
    gstin                       = models.CharField(max_length=100,default='',null=True)
    gst_state_id                = models.CharField(max_length=100,default='32',null=True)
    gst_treatment_id            = models.ForeignKey(gst_treatment_data,on_delete=models.SET_NULL,null=True)
    is_amented                  = models.BooleanField(max_length=100,default=0)
    amented_upward              = models.BooleanField(max_length=100,default=0)
    amented_downward            = models.BooleanField(max_length=100,default=0)
    voucher_number_appended     = models.CharField(max_length=100,null=True)
    branch_gst_state_id         = models.CharField(max_length=100,default='32',null=True)
    branch_gst_treatment_id     = models.ForeignKey(gst_treatment_data,on_delete=models.SET_NULL,null=True,related_name='branch_invoice_treatment')
    additional_subtotal         = models.CharField(max_length=100,default='',null=True)
    tax_value                   = models.TextField(default='',null=True)


class bill_by_bill_data(models.Model):
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    order_id            = models.ForeignKey(order_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    voucher_type_id     = models.ForeignKey(voucher_type_data,on_delete=models.CASCADE,default='',null=True)
    voucher_series_id   = models.ForeignKey(voucher_series_data,on_delete=models.CASCADE,default='',null=True)
    financial_year_id   = models.ForeignKey(financial_year_data,on_delete=models.CASCADE,default='',null=True)
    voucher_number_id   = models.ForeignKey(voucher_number_data,on_delete=models.CASCADE,default='',null=True)
    exchange_rate       = models.CharField(max_length=100,default='',null=True)
    date                = models.CharField(max_length=100,default='',null=True)
    due_date            = models.CharField(max_length=100,default='',null=True)
    due_days            = models.CharField(max_length=100,default='',null=True)
    description         = models.TextField(default='',null=True)
    total_amount        = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    invoice_id          = models.ForeignKey(invoice_data,on_delete=models.CASCADE,default='',null=True)
    debit_ledger_id     = models.ForeignKey(accounting_ledger_data,on_delete=models.CASCADE,default='',null=True, related_name='bill_debit_ledger_id')
    credit_ledger_id    = models.ForeignKey(accounting_ledger_data,on_delete=models.CASCADE,default='',null=True, related_name='bill_credit_ledger_id')
    created_by          = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True, related_name='bill_created_by')
    approved_by         = models.ForeignKey(user_data,on_delete=models.CASCADE,default='',null=True, related_name='bill_approved_by')
    status              = models.CharField(max_length=100,default='',null=True)
    close               = models.BooleanField(max_length=100,default=0)
    close_invoice_id    = models.ForeignKey(invoice_data,on_delete=models.CASCADE,default='',null=True, related_name='close_invoice_id')
    bill_description    = models.TextField(default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')


class order_product_data(models.Model):
    order_id            = models.ForeignKey(order_data,on_delete=models.CASCADE,default='',null=True)
    invoice_id          = models.ForeignKey(invoice_data,on_delete=models.CASCADE,default='',null=True)
    branch_id           = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    batch_id            = models.ForeignKey(batch_data,on_delete=models.CASCADE,default='',null=True)
    entity_id           = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    product_id          = models.ForeignKey(product_data,on_delete=models.CASCADE,default='',null=True)
    unit_id             = models.ForeignKey(unit_data,on_delete=models.CASCADE,default='',null=True)
    godown_id           = models.ForeignKey(godown_data,on_delete=models.CASCADE,default='',null=True)
    rack_id             = models.ForeignKey(rack_data,on_delete=models.CASCADE,default='',null=True)
    tax_id              = models.ForeignKey(tax_data,on_delete=models.CASCADE,default='',null=True)
    product_code        = models.CharField(max_length=100,default='',null=True)
    quantity            = models.CharField(max_length=100,default='',null=True)
    free                = models.CharField(max_length=100,default='',null=True)
    po_quantity         = models.CharField(max_length=100,default='',null=True) ##purchase order
    so_quantity         = models.CharField(max_length=100,default='',null=True) ##sales order
    purchase_rate       = models.CharField(max_length=100,default='',null=True)
    tax_amount          = models.CharField(max_length=100,default='',null=True)
    product_rate        = models.CharField(max_length=100,default='',null=True)
    amount              = models.CharField(max_length=100,default='',null=True)
    discount_type       = models.CharField(max_length=100,default='',null=True)
    discount            = models.CharField(max_length=100,default='',null=True)
    entry_type          = models.CharField(max_length=100,default='',null=True)
    order_product_id    = models.ForeignKey('self', on_delete=models.CASCADE, default='', null=True, related_name='edit_invoice_prodcut')
    cgst                = models.CharField(max_length=100,default='',null=True)
    sgst                = models.CharField(max_length=100,default='',null=True)
    igst                = models.CharField(max_length=100,default='',null=True)
    pretax_amount       = models.CharField(max_length=100,default='',null=True)
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')
    # additional
    reverse_tax         = models.CharField(max_length=100,default='',null=True)
    reverse_tax_value   = models.CharField(max_length=100,default='',null=True)
    reverse_cgst        = models.CharField(max_length=100,default='',null=True)
    reverse_sgst        = models.CharField(max_length=100,default='',null=True)
    reverse_igst                = models.TextField(default='',null=True)
    hsn                 = models.CharField(max_length=100,default='')
    sac                 = models.CharField(max_length=100,default='')
    voucher_type_id     = models.ForeignKey(voucher_type_data,on_delete=models.CASCADE,default='',null=True)
    estiamted_quantity  = models.CharField(max_length=100,default='')
    performa_quantity   = models.CharField(max_length=100,default='')
    financial_year_id   = models.ForeignKey(financial_year_data,on_delete=models.SET_NULL,null=True)
    voucher_number_id   = models.ForeignKey(voucher_number_data,on_delete=models.CASCADE,default='',null=True)
    # additional
    additional_charge   = models.BooleanField(max_length=100,default=0)
    tax_value           = models.CharField(max_length=100,default='')
    latest              = models.BooleanField(max_length=100,default=0)
    status              = models.CharField(max_length=100,default='Pending',null=True)
    date                = models.DateTimeField(blank=True, null=True)
    product_group       = models.ForeignKey(product_group_data,on_delete=models.SET_NULL,null=True)    
    
    def save(self, *args, **kwargs):
        if self.product_id:
            self.product_group = self.product_id.product_group_id
        super().save(*args, **kwargs)


class additional_cost_data(models.Model):
    order_id                        = models.ForeignKey(order_data,on_delete=models.CASCADE,default='',null=True)
    invoice_id                      = models.ForeignKey(invoice_data,on_delete=models.CASCADE,default='',null=True)
    branch_id                       = models.ForeignKey(branch_data,on_delete=models.CASCADE,default='',null=True)
    entity_id                       = models.ForeignKey(entity_data,on_delete=models.CASCADE,default='',null=True)
    product_id                      = models.ForeignKey(product_data,on_delete=models.CASCADE,default='',null=True)
    amount                          = models.CharField(max_length=100,default='',null=True)
    created_at                      = models.DateTimeField(max_length=100,default='')
    updated_at                      = models.DateTimeField(max_length=100,default='')


class golden_rules(models.Model):
    voucher_type_id             = models.ForeignKey(voucher_type_data,on_delete=models.CASCADE,default='',null=True)
    debit_account_group_ids     = models.TextField(default='',null=True)
    credit_account_group_ids    = models.TextField(default='',null=True)
    created_at                  = models.DateTimeField(max_length=100,default='')
    updated_at                  = models.DateTimeField(max_length=100,default='')



class app_auth_token_tb(models.Model):
    token               = models.CharField(max_length=100,default='')
    created_at          = models.DateTimeField(max_length=100,default='')
    updated_at          = models.DateTimeField(max_length=100,default='')



class custom_reports(models.Model):
    name                        = models.TextField(default='',null=True)
    table_name                  = models.TextField(default='',null=True)
    filter_financial_year       = models.BooleanField(default=0)
    filter_voucher_type         = models.ForeignKey(voucher_type_data,on_delete=models.SET_NULL,default='',null=True,blank=True)
    filter_branch               = models.BooleanField(default=0)
    filter_entity               = models.BooleanField(default=0)
    

class custom_reports_fields(models.Model):
    custom_report               = models.ForeignKey(custom_reports,on_delete=models.CASCADE,related_name='get_fields')
    label                       = models.TextField(default='',null=True)
    field_name                  = models.TextField(default='',null=True)
    field_type                  = models.TextField(default='',null=True) 
    model_name                  = models.TextField(default='',null=True)
    fkfield                     = models.TextField(default='',null=True)
    add_on_report               = models.BooleanField(max_length=100,default=0)     
    add_filter                  = models.BooleanField(max_length=100,default=0)
    default_filter              = models.TextField(default='',null=True)   
    apply_sum                   = models.BooleanField(max_length=100,default=0)    


