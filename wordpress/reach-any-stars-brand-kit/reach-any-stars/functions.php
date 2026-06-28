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
	wp_enqueue_style(
		'reach-any-stars',
		get_stylesheet_uri(),
		array(),
		wp_get_theme()->get( 'Version' )
	);
}, 20 );
