<?php
/**
 * Reach Any Stars — standalone block theme bootstrap.
 *
 * Brand colors, Manrope typography (self-hosted), spacing, element and
 * WooCommerce styles all live in theme.json — the single source of truth.
 * The Manrope @font-face is generated automatically by WordPress from the
 * fontFace entry in theme.json, so no manual font enqueue is needed.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'after_setup_theme', function () {
	// Block theme niceties.
	add_theme_support( 'wp-block-styles' );      // default styling for core blocks
	add_theme_support( 'editor-styles' );        // apply style.css inside the editor
	add_theme_support( 'responsive-embeds' );
	add_editor_style( 'style.css' );

	// WooCommerce: declare support so Woo uses our block templates + galleries.
	add_theme_support( 'woocommerce' );
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-slider' );
} );

// Load style.css on the front end for any hand-written CSS overrides.
add_action( 'wp_enqueue_scripts', function () {
	// Version by file mtime so edits bust the browser cache automatically
	// (no more stale CSS after a change). Falls back to the theme version.
	$style_path = get_stylesheet_directory() . '/style.css';
	$style_ver  = file_exists( $style_path ) ? filemtime( $style_path ) : wp_get_theme()->get( 'Version' );
	wp_enqueue_style(
		'reach-any-stars',
		get_stylesheet_uri(),
		array(),
		$style_ver
	);
}, 20 );

// Account menu: we're already inside the account area, so "Account details"
// reads better as simply "Details".
add_filter( 'woocommerce_account_menu_items', function ( $items ) {
	if ( isset( $items['edit-account'] ) ) {
		$items['edit-account'] = __( 'Details', 'reach-any-stars' );
	}
	return $items;
} );
