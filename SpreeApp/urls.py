from django.urls import path,include
from SpreeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.userLogin ,name='user-login'),
    path('user-logout/', views.userLogout ,name='user-logout'),
    path('update-user-profile',views.updateUserProfile,name='update-user-profile'),

    path('user-dashboard/', views.userDashboard ,name='user-dashboard'),
    
    path('list-entity-type/', views.listEntityType ,name='list-entity-type'),
    path('add-entity-type/', views.addNewEntityType ,name='add-entity-type'),
    path('update-entity-type/', views.updateEntityType ,name='update-entity-type'),
    path('delete-entity-type/', views.deleteEntityType ,name='delete-entity-type'),
    path('view-entity-type/', views.viewEntityType ,name='view-entity-type'),


    path('list-entity-category/', views.listEntityCategory ,name='list-entity-category'),
    path('add-entity-category/', views.addNewEntityCategory ,name='add-entity-category'),
    path('update-entity-category/', views.updateEntityCategory ,name='update-entity-category'),
    path('delete-entity-category/', views.deleteEntityCategory ,name='delete-entity-category'),

    path('list-entity/', views.listEntity ,name='list-entity'),
    path('add-entity/', views.addNewEntity ,name='add-entity'),
    path('update-entity/', views.updateEntity ,name='update-entity'),
    path('delete-entity/', views.deleteEntity ,name='delete-entity'),

    path('list-branch/', views.listBanch ,name='list-branch'),
    path('add-branch/', views.addNewBranch ,name='add-branch'),
    path('update-branch/', views.updateBranch ,name='update-branch'),
    path('delete-branch/', views.deleteBranch ,name='delete-branch'),
    path('get-branchs/', views.get_branchs ,name='get_branchs'),
    path('get-branchs-details/', views.get_branch_details ,name='get-branchs-details'),

    

    path('list-user-roles/', views.listUserRole ,name='list-user-roles'),
    path('add-user-role/', views.addNewUserRole ,name='add-user-role'),
    path('update-user-role/', views.updateUserRole ,name='update-user-role'),
    path('delete-user-role/', views.deleteUserRole ,name='delete-user-role'),

    path('list-user/', views.listUsers ,name='list-user'),
    path('add-user/', views.addNewUser ,name='add-user'),
    path('update-user/', views.updateUser ,name='update-user'),
    path('delete-user/', views.deleteUser ,name='delete-user'),
    

    path('list-user-role-permissions/', views.listUserRolePermissions ,name='list-user-role-permissions'),
    path('update-user-role-permission/', views.updateUserRolePermission ,name='update-user-role-permission'),

    path('get-entity-branch/', views.getEntityBranch ,name='get-entity-branch'),
    path('get-single-entity-branch/', views.getSingleEntityBranch ,name='get-single-entity-branch'),
    path('set-default-entity/', views.setDefaultUserEntity ,name='set-default-entity'),


    path('list-accounting-group/', views.listAccountingGroup ,name='list-accounting-group'),
    path('add-accounting-group/', views.addNewAccountingGroup ,name='add-accounting-group'),
    path('update-accounting-group/', views.updateAccountingGroup ,name='update-accounting-group'),
    path('delete-accounting-group/', views.deleteAccountingGroup ,name='delete-accounting-group'),
    path('get-accounting-group',views.getAccountingGroup,name='get-accounting-group'),

    path('list-accounting-ledger/', views.listAccountingLedger ,name='list-accounting-ledger'),
    path('add-accounting-ledger/', views.addNewAccountingLedger ,name='add-accounting-ledger'),
    path('update-accounting-ledger/', views.updateAccountingLedger ,name='update-accounting-ledger'),
    path('delete-accounting-ledger/', views.deleteAccountingLedger ,name='delete-accounting-ledger'),
    path('get-AccountLedger-balance',views.get_AccountLedger_balance,name='get-AccountLedger-balance'),

    path('getProduct-balance',views.getProduct_balance,name='getProduct-balance'),

    path('list-financial-year/', views.listFinancialYear ,name='list-financial-year'),
    path('add-financial-year/', views.addNewFinancialYear ,name='add-financial-year'),
    path('update-financial-year/', views.updateFinancialYear ,name='update-financial-year'),
    path('delete-financial-year/', views.deleteFinancialYear ,name='delete-financial-year'),


    path('list-series/', views.listSeries ,name='list-series'),
    path('add-series/', views.addNewSeries ,name='add-series'),
    path('update-series/', views.updateSeries ,name='update-series'),
    path('delete-series/', views.deleteSeries ,name='delete-series'),


    path('list-customer-type/', views.listCustomerType ,name='list-customer-type'),
    path('add-customer-type/', views.addNewCustomerType ,name='add-customer-type'),
    path('update-customer-type/', views.updateCustomerType ,name='update-customer-type'),
    path('delete-customer-type/', views.deleteCustomerType ,name='delete-customer-type'),


    path('list-location/', views.listLocation ,name='list-location'),
    path('add-location/', views.addNewLocation ,name='add-location'),
    path('update-location/', views.updateLocation ,name='update-location'),
    path('delete-location/', views.deleteLocation ,name='delete-location'),


    path('list-customer/', views.listCustomer ,name='list-customer'),
    path('add-customer/', views.addNewCustomer ,name='add-customer'),
    path('get-customer-data/',views.get_customer_details,name='get-customer-data'),
    path('update-customer/', views.updateCustomer ,name='update-customer'),
    path('delete-customer/', views.deleteCustomer ,name='delete-customer'),

    path('list-supplier-type/', views.listSupplierType ,name='list-supplier-type'),
    path('add-supplier-type/', views.addNewSupplierType ,name='add-supplier-type'),
    path('get-supplier-data/',views.get_supplier_details,name='get-supplier-data'),
    path('update-supplier-type/', views.updateSupplierType ,name='update-supplier-type'),
    path('delete-supplier-type/', views.deleteSupplierType ,name='delete-supplier-type'),


    path('list-supplier/', views.listSupplier ,name='list-supplier'),
    path('add-supplier/', views.addNewSupplier ,name='add-supplier'),
    path('update-supplier/', views.updateSupplier ,name='update-supplier'),
    path('delete-supplier/', views.deleteSupplier ,name='delete-supplier'),


    path('list-unit/', views.listUnit ,name='list-unit'),
    path('add-unit/', views.addNewUnit ,name='add-unit'),
    path('update-unit/', views.updateUnit ,name='update-unit'),
    path('delete-unit/', views.deleteUnit ,name='delete-unit'),

    path('list-size/', views.listSize ,name='list-size'),
    path('add-size/', views.addNewSize ,name='add-size'),
    path('update-size/', views.updateSize ,name='update-size'),
    path('delete-size/', views.deleteSize ,name='delete-size'),


    path('list-brand/', views.listBrand ,name='list-brand'),
    path('add-brand/', views.addNewBrand ,name='add-brand'),
    path('update-brand/', views.updateBrand ,name='update-brand'),
    path('delete-brand/', views.deleteBrand ,name='delete-brand'),


    path('list-model-number/', views.listModelNumber ,name='list-model-number'),
    path('add-model-number/', views.addNewModelNumber ,name='add-model-number'),
    path('update-model-number/', views.updateModelNumber ,name='update-model-number'),
    path('delete-model-number/', views.deleteModelNumber ,name='delete-model-number'),


    path('list-godown/', views.listGodown ,name='list-godown'),
    path('add-godown/', views.addNewGodown ,name='add-godown'),
    path('update-godown/', views.updateGodown ,name='update-godown'),
    path('delete-godown/', views.deleteGodown ,name='delete-godown'),
    path('get-godowns/',views.get_godowns,name='get-godowns'),
    path('get-Godowns',views.getGodowns,name='get-Godowns'),



    path('list-rack/', views.listRack ,name='list-rack'),
    path('add-rack/', views.addNewRack ,name='add-rack'),
    path('update-rack/', views.updateRack ,name='update-rack'),
    path('delete-rack/', views.deleteRack ,name='delete-rack'),


    path('list-product-group/', views.listProductGroup ,name='list-product-group'),
    path('add-product-group/', views.addNewProductGroup ,name='add-product-group'),
    path('update-product-group/', views.updateProductGroup ,name='update-product-group'),
    path('delete-product-group/', views.deleteProductGroup ,name='delete-product-group'),


    path('list-pricing-level/', views.listPricingLevel ,name='list-pricing-level'),
    path('add-pricing-level/', views.addNewPricingLevel ,name='add-pricing-level'),
    path('update-pricing-level/', views.updatePricingLevel ,name='update-pricing-level'),
    path('delete-pricing-level/', views.deletePricingLevel ,name='delete-pricing-level'),


    path('list-tax-data/', views.listTaxData ,name='list-tax-data'),
    path('add-tax-data/', views.addNewTaxData ,name='add-tax-data'),
    path('update-tax-data/', views.updateTaxData ,name='update-tax-data'),
    path('delete-tax-data/', views.deleteTaxData ,name='delete-tax-data'),

    path('get-tax-data/', views.gettax ,name='get-tax-data'),

    path('list-product/', views.listProducts ,name='list-product'),
    path('add-product/', views.addNewProduct ,name='add-product'),
    path('update-product/', views.updateProduct ,name='update-product'),
    path('delete-product/', views.deleteProduct ,name='delete-product'),
    path('get-product',views.getproducts,name='get-product'),



    path('list-voucher-type/', views.listVoucherType ,name='list-voucher-type'),
    path('add-voucher-type/', views.addNewVoucherType ,name='add-voucher-type'),
    path('update-voucher-type/', views.updateVoucherType ,name='update-voucher-type'),
    path('delete-voucher-type/', views.deleteVoucherType ,name='delete-voucher-type'),


    path('list-voucher-series/', views.listVoucherSeries ,name='list-voucher-series'),
    path('add-voucher-series/', views.addNewVoucherSeries ,name='add-voucher-series'),
    path('update-voucher-series/', views.updateVoucherSeries ,name='update-voucher-series'),
    path('delete-voucher-series/', views.deleteVoucherSeries ,name='delete-voucher-series'),


    path('list-warehouse/', views.listWareHouse ,name='list-warehouse'),
    path('add-warehouse/', views.addNewWarehouse ,name='add-warehouse'),
    path('update-warehouse/', views.updateWarehouse ,name='update-warehouse'),
    path('delete-warehouse/', views.deleteWarehouse ,name='delete-warehouse'),


    path('list-batch/', views.listBatch ,name='list-batch'),
    path('add-batch/', views.addNewBatch ,name='add-batch'),
    path('update-batch/', views.updateBatch ,name='update-batch'),
    path('delete-batch/', views.deleteBatch ,name='delete-batch'),
    

    path('list-purchase-order/', views.listPurchaseOrder ,name='list-purchase-order'),
    path('add-purchase-order/', views.addNewPurchaseOrder ,name='add-purchase-order'),
    path('update-purchase-order/', views.updatePurchaseOrder ,name='update-purchase-order'),
    path('delete-purchase-order/', views.deletePurchaseOrder ,name='delete-purchase-order'),
    path('delete-order-purchase-product/', views.deletePurchaseOrderProduct ,name='delete-order-purchase-product'),

    path('list-purchase-invoice/', views.listPurchaseInvoice,name='list-purchase-invoice'),
    path('add-purchase-invoice/', views.addPurchaseInvoice,name='add-purchase-invoice'),
    path('generate-purchase-invoice/', views.generatePurchaseInvoice,name='generate-purchase-invoice'),
    path('delete-order-purchase-product-invoice/', views.deletePurchaseOrderProductInvoice ,name='delete-order-purchase-product-invoice'),
    path('update-purchase-invoice/', views.updatePurchaseInvoice,name='update-purchase-invoice'),
    path('list-purchase-invoice-history/', views.listPurchaseInvoiceHistory,name='list-purchase-invoice-history'),

    
    path('get-purchase-voucher-number/', views.getPurchaseVoucherNumber,name='get-purchase-voucher-number'),
    
    path('get-product-data/', views.getProductData ,name='get-product-data'),
    
    path('list-sales-order/', views.listSalesOrder ,name='list-sales-order'),
    path('add-sales-order/', views.addNewSalesOrder ,name='add-sales-order'),
    path('update-sales-order/', views.updateSalesOrder ,name='update-sales-order'),
    path('delete-sales-order/', views.deleteSalesOrder ,name='delete-sales-order'),
    path('delete-order-sales-product/', views.deleteSalesOrderProduct ,name='delete-order-sales-product'),

    path('list-sales-invoice/', views.listSalesInvoice,name='list-sales-invoice'),
    path('add-sales-invoice/', views.addSalesInvoice,name='add-sales-invoice'),
    path('generate-sales-invoice/', views.generateSalesInvoice,name='generate-sales-invoice'),
    path('update-sales-invoice/', views.updateSalesInvoice,name='update-sales-invoice'),
    path('delete-order-sales-product-invoice/', views.deleteSalesOrderProductInvoice ,name='delete-order-sales-product-invoice'),
    # path('delete-sales-invoice/', views.deleteSalesInvoice,name='delete-sales-invoice'),
    path('list-sales-invoice-history/', views.listSalesInvoiceHistory,name='list-sales-invoice-history'),
    

    path('list-payment-voucher/', views.listPaymentVoucher,name='list-payment-voucher'),
    path('add-payment-voucher/', views.addNewPaymentVoucher,name='add-payment-voucher'),
    path('update-payment-voucher/', views.updatePaymentVoucher ,name='update-payment-voucher'),
    path('delete-payment-voucher-ledger/', views.deletePaymentVoucherLedger ,name='delete-payment-voucher-ledger'),
    path('delete-payment-voucher/', views.deletePaymentVoucer ,name='delete-payment-voucher'),


    path('list-receipt-voucher/', views.listReceiptVoucher,name='list-receipt-voucher'),
    path('add-receipt-voucher/', views.addNewReceiptVoucher,name='add-receipt-voucher'),
    path('update-receipt-voucher/', views.updateReceiptVoucher ,name='update-receipt-voucher'),
    path('delete-receipt-voucher-ledger/', views.deleteReceiptVoucherLedger ,name='delete-receipt-voucher-ledger'),
    path('delete-receipt-voucher/', views.deleteReceiptVoucer ,name='delete-receipt-voucher'),


    path('list-contra-voucher/', views.listContraVoucher,name='list-contra-voucher'),
    path('add-contra-voucher/', views.addNewContraVoucher,name='add-contra-voucher'),
    path('update-contra-voucher/', views.updateContraVoucher ,name='update-contra-voucher'),
    path('delete-contra-voucher-ledger/', views.deleteContraVoucherLedger ,name='delete-contra-voucher-ledger'),
    path('delete-contra-voucher/', views.deleteContraVoucer ,name='delete-contra-voucher'),

    path('list-journal-voucher/', views.listJournalVoucher,name='list-journal-voucher'),
    path('add-journal-voucher/', views.addNewJournalVoucher,name='add-journal-voucher'),
    path('update-journal-voucher/', views.updateJournalVoucher ,name='update-journal-voucher'),
    path('delete-journal-voucher-ledger/', views.deleteJournalVoucherLedger ,name='delete-journal-voucher-ledger'),
    path('delete-journal-voucher/', views.deleteJournalVoucer ,name='delete-journal-voucher'),


    path('list-credit-note/', views.listCreditNote,name='list-credit-note'),
    path('add-credit-note/', views.addNewCreditNote,name='add-credit-note'),
    path('update-credit-note/', views.updateCreditNote ,name='update-credit-note'),
    path('delete-credit-note-ledger/', views.deleteCreditNoteLedger ,name='delete-credit-note-ledger'),
    path('delete-credit-note/', views.deleteCreditNote ,name='delete-credit-note'),


    path('list-debit-note/', views.listDebitNote,name='list-debit-note'),
    path('add-debit-note/', views.addNewDebitNote,name='add-debit-note'),
    path('update-debit-note/', views.updateDebitNote ,name='update-debit-note'),
    path('delete-debit-note-ledger/', views.deleteDebitNoteLedger ,name='delete-debit-note-ledger'),
    path('delete-debit-note/', views.deleteDebitNote ,name='delete-debit-note'),

    path('list-golden-rule/', views.listGoldenRules,name='list-golden-rule'),
    path('add-golden-rule/', views.addNewGoldenRule,name='add-golden-rule'),
    path('update-golden-rule/', views.updateGoldenRule,name='update-golden-rule'),
    path('delete-golden-rule/', views.deleteGoldenRule,name='delete-golden-rule'),



    # additional
    path('list-gst-treatment/', views.listGstTreatmentData,name='list-gst-treatment'),
    path('add-gst-treatment/', views.addNewGstTreatmentData,name='add-gst-treatment'),
    path('update-gst-treatment/', views.updateGstTreatment,name='update-gst-treatment'),
    path('delete-gst-treatment/', views.deleteGstTreatment,name='delete-gst-treatment'),

    path('get-godown-rack/', views.getGodownRacks ,name='get-godown-rack'),
    path('get-entity-gst/', views.get_entity_gst,name='get-entity-gst'),







    ##############################--------- Api's ----------------################################

    # path('generate-app-token/', views.appAuthToken,name='generate-app-token'),
    path('user-portal-login/', views.userPortalLogin,name='user-portal-login'),
    
    path('user-portal-add-purchase-order/', views.addPurchaseOrderFromUserPortal,name='user-portal-add-purchase-order'),
    path('user-portal-list-purchase-order/', views.listPurchaseOrderUserPortal ,name='user-portal-list-purchase-order'),
    path('user-portal-update-purchase-order/', views.updatePurchaseOrderUserPortal ,name='user-portal-update-purchase-order'),
    path('user-portal-delete-purchase-order/', views.deletePurchaseOrderUserPortal ,name='user-portal-delete-purchase-order'),
    path('user-portal-delete-order-purchase-product/', views.deletePurchaseOrderProductUserPortal ,name='user-portal-delete-order-purchase-product'),

    path('user-portal-list-purchase-invoice/', views.listPurchaseInvoiceUserPortal,name='user-portal-list-purchase-invoice'),
    path('user-portal-add-purchase-invoice/', views.addPurchaseInvoiceUserPortal,name='user-portal-add-purchase-invoice'),
    path('user-portal-generate-purchase-invoice/', views.generatePurchaseInvoiceUserPortal,name='user-portal-generate-purchase-invoice'),
    path('user-portal-delete-order-purchase-product-invoice/', views.deletePurchaseOrderProductInvoiceUserPortal ,name='user-portal-delete-order-purchase-product-invoice'),
    path('user-portal-update-purchase-invoice/', views.updatePurchaseInvoiceUserPortal,name='user-portal-update-purchase-invoice'),
    
    path('user-portal-list-sales-order/', views.listSalesOrderUserPortal ,name='user-portal-list-sales-order'),
    path('user-portal-add-sales-order/', views.addNewSalesOrderUserPortal ,name='user-portal-add-sales-order'),
    path('user-portal-update-sales-order/', views.updateSalesOrderUserPortal ,name='user-portal-update-sales-order'),
    path('user-portal-delete-order-sales-product/', views.deleteSalesOrderProductUserPortal ,name='user-portal-delete-order-sales-product'),
    path('user-portal-delete-sales-order/', views.deleteSalesOrderUserPortal ,name='user-portal-delete-sales-order'),

    path('user-portal-list-sales-invoice/', views.listSalesInvoiceUserPortal,name='user-portal-list-sales-invoice'),
    path('user-portal-add-sales-invoice/', views.addSalesInvoiceUserPortal,name='user-portal-add-sales-invoice'),
    path('user-portal-generate-sales-invoice/', views.generateSalesInvoiceUserPortal,name='user-portal-generate-sales-invoice'),
    path('user-portal-update-sales-invoice/', views.updateSalesInvoiceUserPortal,name='user-portal-update-sales-invoice'),
    path('user-portal-delete-order-sales-product-invoice/', views.deleteSalesOrderProductInvoiceUserPortal ,name='user-portal-delete-order-sales-product-invoice'),
    

    path('user-portal-list-payment-voucher/', views.listPaymentVoucherUserPortal,name='user-portal-list-payment-voucher'),

    
    path('user-portal-get-branch-data/', views.getUserBranchInUserPortal,name='user-portal-get-branch-data'),
    
    path('user-portal-list-product-units/', views.userPortalListProductUnits,name='user-portal-list-product-units'),

# api filter start
    path('user-portal-entitytype-filter/',views.listEntityTypeUserPortal,name='user-portal-entitytype-filter'),
    path('user-portal-entity-category-filter/',views.listEntityCategoryUserPortal,name='user-portal-entity-category-filter'),
    path('user-portal-entity-filter/',views.listEntityUserPortal,name='user-portal-entity-filter'),
    path('user-portal-branch-filter/',views.listBranchUserPortal,name='user-portal-branch-filter'),
    path('user-portal-user-role-filter/',views.listUserRoleUserPortal,name='user-portal-user-role-filter'),
    path('user-portal-user-filter/',views.listUsersUserPortal,name='user-portal-user-filter'),
    path('user-portal-accountgroup-filter/',views.filterDownloadaccountgroupUserPortal,name='user-portal-accountgroup-filter'),
    path('user-portal-accountledger-filter/',views.filterAccountLedgerUserPortal,name='user-portal-accountledger-filter'),
    path('user-portal-financialyear-filter/',views.filterFinancialYearUserPortal,name='user-portal-financialyear-filter'),
    path('user-portal-series-filter/',views.filterSeriesUserPortal,name='user-portal-series-filter'),
    path('user-portal-customertype-filter/',views.filterCustomerTypeUserPortal,name='user-portal-customertype-filter'),
    path('user-portal-location-filter/',views.filterLocationUserPortal,name='user-portal-location-filter'),
    path('user-portal-customer-filter/',views.filterCustomerUserPortal,name='user-portal-location-filter'),
    path('user-portal-suppliertype-filter/',views.filterSupplier_typeUserPortal,name='user-portal-suppliertype-filter'),
    path('user-portal-supplier-filter/',views.filterSupplierUserPortal,name='user-portal-supplier-filter'),
    path('user-portal-unit-filter/',views.filterUnitUserPortal,name='user-portal-unit-filter'),
    path('user-portal-size-filter/',views.filterSizeUserPortal,name='user-portal-size-filter'),
    path('user-portal-brand-filter/',views.filterBrandUserPortal,name='user-portal-brand-filter'),
    path('user-portal-model-filter/',views.filterModelUserPortal,name='user-portal-model-filter'),
    path('user-portal-godown-filter/',views.filterGodownUserPortal,name='user-portal-godown-filter'),
    path('user-portal-rack-filter/',views.filterRackUserPortal,name='user-portal-rack-filter'),
    path('user-portal-productgrp-filter/',views.filterProductGroupUserPortal,name='user-portal-productgrp-filter'),
    path('user-portal-pricelevel-filter/',views.filterPriceLvlUserPortal,name='user-portal-pricelevel-filter'),
    path('user-portal-product-filter/',views.filterProductUserPortal,name='user-portal-product-filter'),
    path('user-portal-vouchertype-filter/',views.filterVoucherTypeUserPortal,name='user-portal-vouchertype-filter'),
    path('user-portal-voucherseries-filter/',views.filterVoucherSeriesUserPortal,name='user-portal-voucherseries-filter'),
    path('user-portal-tax-filter/',views.filterTaxUserPortal,name='user-portal-tax-filter'),
    path('user-portal-warehouse-filter/',views.filterWarehouseUserPortal,name='user-portal-warehouse-filter'),
    path('user-portal-batch-filter/',views.filterBatcheUserPortal,name='user-portal-batch-filter'),
    path('user-portal-purchaseorder-filter/',views.filterPurchaseOrderPortal,name='user-portal-purchaseorder-filter'),
    path('user-portal-purchaseinvoice-filter/',views.filterPurchaseInvoicePortal,name='user-portal-purchaseinvoice-filter'),
    path('user-portal-salesorder-filter/',views.filterSalesOrderPortal,name='user-portal-salesorder-filter'),
    path('user-portal-salesinvoice-filter/',views.filterSalesInvoicePortal,name='user-portal-salesinvoice-filter'),
    path('user-portal-paymentvoucher-filter/',views.filterPaymentVoucherInvoicePortal,name='user-portal-paymentvoucher-filter'),
    path('user-portal-receipttvoucher-filter/',views.filterReceiptVoucherPortal,name='user-portal-receipttvoucher-filter'),
    path('user-portal-creditnote-filter/',views.filterCreditnotePortal,name='user-portal-creditnote-filter'),
    path('user-portal-debitnote-filter/',views.filterDebitNotenotePortal,name='user-portal-debitnote-filter'),
    path('user-portal-goldenrule-filter/',views.filterGoldenRulePortal,name='user-portal-goldenrule-filter'),
    path('user-portal-journal-filter/',views.filterJournalUserPortal,name='user-portal-journal-filter'),
    path('user-portal-contra-filter/',views.filterContraUserPortal,name='user-portal-contra-filter'),


    # api filter end

    path('get-previous-product-data/', views.getPreviousProductData ,name='get-previous-product-data'), 
    path('get-available-product-quatity/', views.getAvailableProductQuantity ,name='get-available-product-quatity'),



    # additional apis
    path('user-portal-get-productdata',views.userPortalgetProductData,name='user-portal-get-productdata'),
    path('user-portal-get-previous-ProductData',views.UserportalGetPreviousProductData,name='user-portal-get-previous-ProductData'),
    path('user-portal-get-availableProductQuauntity',views.UserPortalgetAvailableProductQuantity,name='user-portal-get-availableProductQuauntity'),
    path('user-portal-add-product',views.UserPortalAddProduct,name='user-portal-add-product'),
    path('user-portal-add-batch',views.UserPortalAddBatch,name='user-portal-add-batch'),
    path('user-portal-get-bill',views.get_bill_by_bill,name='user-portal-get-bill'),
    path('user-portal-get-actledger',views.get_account_ledgers,name='user-portal-get-actledger'),
    path('user-portal-get-accountledger_of_supplier_customer',views.UserPortalget_ledger_of_supplier_customer,name='user-portal-get-accountledger_of_supplier_customer'),
    
    path('user-portal-expenseledger',views.userPortalgetExpenseLedger,name='user-portal-expenseledger'),
    
    
    # transactions
    path('user-portal-addpayment-voucher',views.UserPortalAddPaymentVoucher,name='user-portal-addpayment-voucher'),
    


    

    # view pages
    path('view-entity-category/',views.viewEntityCategory,name='view-entity-category'),
    path('view-entity/',views.viewEntity,name='view-entity'),
    path('view-user-role/',views.ViewUserRole,name='view-user-role'),
    path('view-user/',views.ViewUser,name='view-user'), 
    path('view-accounting-group/',views.ViewAccountingGroup,name='view-accounting-group'),
    path('view-accounting-ledger/',views.ViewAccountingLedger,name='view-accounting-ledger'),
    path('view-financial-year/',views.ViewFinancialYear,name='view-financial-year'),
    path('view-series/',views.ViewSeries,name='view-series'),
    path('view-customer-type/',views.ViewCustomerType,name='view-customer-type'),
    path('view-location/',views.ViewLocation,name='view-location'),
    path('view-customer/',views.ViewCustomer,name='view-customer'),
    path('view-supplier-type/',views.ViewSupplierType,name='view-supplier-type'),
    path('view-supplier/',views.ViewSupplier,name='view-supplier'),
    path('view-unit/',views.ViewUnit,name='view-unit'),
    path('view-size/',views.ViewSize,name='view-size'),
    path('view-brand/',views.ViewBrand,name='view-brand'),
    path('view-modelnumber/',views.ViewModelNumber,name='view-modelnumber'),
    path('view-godown/',views.ViewGodown,name='view-godown'),
    path('view-rack/',views.ViewRack,name='view-rack'),
    path('view-productgrp/',views.ViewProductGroup,name='view-productgrp'),
    path('view-pricinglvl/',views.ViewPricingLevel,name='view-pricinglvl'),
    path('view-product/',views.ViewProduct,name='view-product'),
    path('view-vouchertype/',views.ViewVoucherType,name='view-vouchertype'),
    path('view-voucher-series/',views.ViewVoucherSeries,name='view-voucher-series'),
    path('view-tax/',views.ViewTaxData,name='view-tax'),
    path('view-batch/',views.ViewBatch,name='view-batch'),
    path('view-purchase_order/',views.ViewPurchaseOrder,name='view-purchase_order'),
    path('view-purchase-invoice/',views.ViewPurchaseInvoice,name='view-purchase-invoice'),
    path('view-sale-order/',views.ViewSalesOrder,name='view-sale-order'),
    path('view-sale-invoice/',views.ViewSalesInvoice,name='view-sale-invoice'),
    path('view-payment-voucher/',views.ViewPaymentVoucher,name='view-payment-voucher'),
    path('view-receipt-voucher/',views.ViewReceiptVoucher,name='view-receipt-voucher'),
    path('view-contra-voucher/',views.viewContraVoucher,name='view-contra-voucher'),
    path('view-journal/',views.ViewJournalVoucher,name='view-journal'),
    path('view-creditnote/',views.ViewCreditNote,name='view-creditnote'),
    path('view-debitnote/',views.ViewDebitNote,name='view-debitnote'),
    path('view-warehouse/',views.ViewWarehouse,name='view-warehouse'),
    path('view-userpermission/',views.ViewUserRolePermission,name='view-userpermission'),


    
    # view page end


    # report 
    path('report-stock-summary/',views.report_stock_summary,name='report-stock-summary'),
    path('report-low-stock-summary/',views.report_lowstock_summary,name='report-low-stock-summary'),
    path('report-stock-summary-category/',views.report_stock_summary_category,name='report-stock-summary-category'),
    path('report-daybook/',views.report_daybook,name='report-daybook'),
    path('report-balancesheet/',views.report_balance_sheet,name='report-balancesheet'),
    path('report-account_group/',views.report_account_group,name='report-account_group'),
    path('report-account-ledger/',views.report_account_ledger,name='report-account-ledger'),
    path('report-profit-andloss/',views.report_profit_andloss,name='report-profit-andloss'),
    path('report-gstr1/',views.report_gstr1,name='report-gstr1'),
    path('report-gstr2/',views.report_gstr2,name='report-gstr2'),
    path('report-trail-balance/',views.report_trail_balance,name='report-trail-balance'),
    path('report-gstn3b/',views.report_gstn3,name='report-gstn3b'),
    path('report-gstn9/',views.report_gstn9,name='report-gstn9'),



    path('get-pricing-level/', views.get_pricing_level,name='get-pricing-level'),
    path('get-account-nature/', views.get_acc_nature,name='get-account-nature'),

    path('voucher-series-user-portal/',views.getVoucherSeriesUserPortal,name='voucher-series-user-portal'),

    path('add-voucher-transaction-user-portal/',views.addVoucherTransactionUserPortal,name='add-voucher-transaction-user-portal'),
    path('list-voucher-transaction-user-portal/',views.listVoucherTransactionUserPortal,name='list-voucher-transaction-user-portal'),
    path('get-voucher-transaction-user-portal/',views.getVoucherTransactionUserPortal,name='get-voucher-transaction-user-portal'),
    path('update-voucher-transaction-user-portal/',views.updateVoucherTransactionUserPortal,name='update-voucher-transaction-user-portal'),
# get data for update
    path('get-invoice-details',views.getInvoiceDetails,name='get-invoice-details'),
    path('get-latest-voucher-series-number',views.get_latest_voucher_series_number,name='get-latest-voucher-series-number'),

    path('get-Other-vouchers',views.getOtherVouchers,name='get-Other-vouchers'),


    path('addnew-custom-report',views.addnewcustom_report,name='addnew-custom-report'),
    path('get-table-fields',views.get_table_fields,name='get-table-fields'),
    path('view-custom-report',views.view_custom_report,name='view-custom-report'),
    path('list-custom-reports',views.listcustom_reports,name='list-custom-reports'),
    path('update-custom-report',views.updatecustomreport,name='update-custom-report'),
    path('delete-custom-report',views.deletecustomreport,name='delete-custom-report'),
    path('userforgot-password',views.userforgot_password,name='userforgot-password'),
    path('user-reset-password',views.userreset_password,name='user-reset-password'),




    path('get-user-details',views.getUserUserPortal,name='get-user-details'),
    path('update-user-userportal',views.updateUserUserPortal,name='update-user-userportal')

    

]    



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)