<?php
/**
 * Reach Any Stars — child theme bootstrap.
 *
 * Brand colors, Manrope typography (self-hosted), spacing and element styles
 * are all defined in theme.json and merge on top of the parent block theme.
 * The Manrope @font-face is generated automatically by WordPress from the
 * fontFace entry in theme.json — no manual enqueue needed.
 *
 * This file only ensures style.css loads so any hand-written CSS overrides apply.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style(
		'reach-any-stars',
		get_stylesheet_uri(),
		array(),
		wp_get_theme()->get( 'Version' )
	);
}, 20 );
