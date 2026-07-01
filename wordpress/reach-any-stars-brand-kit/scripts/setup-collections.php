<?php
/**
 * Create the star "Collections" and assign each current product to its star.
 * (Collections are a design line that can later span many product types.)
 * Requires the ras_collection taxonomy (registered in the theme functions.php).
 * Run: wp eval-file /wordpress/wp-content/uploads/setup-collections.php --user=1
 */
if ( ! taxonomy_exists( 'ras_collection' ) ) { echo "ras_collection taxonomy not registered\n"; return; }

// product_id => [Collection name, slug]
$map = array(
	16 => array( 'Atlas', 'atlas' ),
	15 => array( 'Comet', 'comet' ),
	12 => array( 'Luna',  'luna'  ),
	14 => array( 'Nova',  'nova'  ),
	11 => array( 'Orion', 'orion' ),
	13 => array( 'Vega',  'vega'  ),
);

foreach ( $map as $pid => $c ) {
	list( $name, $slug ) = $c;
	if ( ! term_exists( $slug, 'ras_collection' ) ) {
		wp_insert_term( $name, 'ras_collection', array( 'slug' => $slug ) );
	}
	wp_set_object_terms( $pid, $slug, 'ras_collection', false );
	echo "assigned product {$pid} -> {$name}\n";
}
echo "done\n";
