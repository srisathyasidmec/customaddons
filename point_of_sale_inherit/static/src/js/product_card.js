import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card"
//import { ProductChangeQuantity } from "@stock/wizard/stock_change_product_qty"
import { patch } from "@web/core/utils/patch";

patch(ProductCard, {
    props: {
        ...ProductCard.props,
        barcode : String ,
        lst_price : { type: Number, optional : true},
    },
})

//export class MyCustomWizard extends ProductChangeQuantity {
//    super.ProductChangeQuantity()
//}
//patch(MyCustomWizard, {
//    props: {
//        ...ProductCard.props,
//        new_quantity : { type: Number, optional : true},
//    },
//})