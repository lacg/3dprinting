<?php
/**
 * Build the Orion Faceted Planter (product 11) as a variable product.
 * Attributes: Size (cm) x Filament (colour+finish spool). Per-variation SKU +
 * price from the SKU legend. Made-to-order (no stock tracking). Idempotent.
 * Run: wp eval-file /wordpress/wp-content/uploads/build-planter.php --user=1
 */
if ( ! function_exists( 'wc_get_product' ) ) { echo "WooCommerce not loaded\n"; return; }

$pid = 11;

$sizes  = array( '8 cm', '12 cm', '20 cm' );
$spools = array( 'Purple Silk', 'Black Matte', 'White Satin' );

$price  = array( '8 cm' => '24', '12 cm' => '32', '20 cm' => '44' );
$scode  = array( '8 cm' => '008', '12 cm' => '012', '20 cm' => '020' );
$spcode = array(
	'Purple Silk' => array( 'PURPLE', 'SILK' ),
	'Black Matte' => array( 'BLACK', 'MATTE' ),
	'White Satin' => array( 'WHITE', 'SATIN' ),
);

// Make it a variable product.
wp_set_object_terms( $pid, 'variable', 'product_type' );
$product = wc_get_product( $pid );

$a_size = new WC_Product_Attribute();
$a_size->set_name( 'Size' );
$a_size->set_options( $sizes );
$a_size->set_visible( true );
$a_size->set_variation( true );
$a_size->set_position( 0 );

$a_fil = new WC_Product_Attribute();
$a_fil->set_name( 'Filament' );
$a_fil->set_options( $spools );
$a_fil->set_visible( true );
$a_fil->set_variation( true );
$a_fil->set_position( 1 );

$product->set_attributes( array( $a_size, $a_fil ) );
$product->set_manage_stock( false );
$product->set_stock_status( 'instock' );
$product->set_sku( 'RAS-PLANTR-ORION' );   // parent base SKU
$product->save();

// Clear any existing variations (so re-running is clean).
foreach ( $product->get_children() as $cid ) {
	wp_delete_post( $cid, true );
}

$made = 0;
foreach ( $sizes as $s ) {
	foreach ( $spools as $sp ) {
		$v = new WC_Product_Variation();
		$v->set_parent_id( $pid );
		$v->set_attributes( array( 'size' => $s, 'filament' => $sp ) );
		list( $col, $fin ) = $spcode[ $sp ];
		$sku = "RAS-PLANTR-ORION-{$scode[$s]}-{$col}-{$fin}";
		$v->set_sku( $sku );
		$v->set_regular_price( $price[ $s ] );
		$v->set_manage_stock( false );
		$v->set_stock_status( 'instock' );
		$v->save();
		echo "OK  {$sku}  \${$price[$s]}\n";
		$made++;
	}
}

WC_Product_Variable::sync( $pid );
wc_delete_product_transients( $pid );
echo "done — {$made} variations\n";
