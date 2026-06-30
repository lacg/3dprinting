<?php
/**
 * My Account dashboard — Reach Any Stars brand-voice override.
 *
 * Overrides woocommerce/myaccount/dashboard.php. Keeps the WooCommerce action
 * hooks so other plugins still work; only the greeting copy is rebranded.
 *
 * @see https://woocommerce.com/document/template-structure/
 */

defined( 'ABSPATH' ) || exit;

/**
 * My Account dashboard.
 *
 * @since 2.6.0
 */
do_action( 'woocommerce_before_account_dashboard' );

$ras_logout_url = function_exists( 'wc_logout_url' ) ? wc_logout_url() : wp_logout_url();
?>

<p>
	<?php
	printf(
		wp_kses(
			/* translators: 1: user display name 2: logout url */
			__( 'Hello %1$s. Good to have you here. <span class="ras-muted">(Not you? <a href="%2$s">Log out</a>)</span>', 'reach-any-stars' ),
			array(
				'a'    => array( 'href' => array() ),
				'span' => array( 'class' => array() ),
			)
		),
		'<strong>' . esc_html( wp_get_current_user()->display_name ) . '</strong>',
		esc_url( $ras_logout_url )
	);
	?>
</p>

<p>
	<?php
	printf(
		wp_kses(
			/* translators: 1: orders url 2: addresses url 3: account details url */
			__( 'From here you can follow your <a href="%1$s">orders</a>, keep your <a href="%2$s">addresses</a> tidy, and update your <a href="%3$s">details</a> whenever you like.', 'reach-any-stars' ),
			array( 'a' => array( 'href' => array() ) )
		),
		esc_url( wc_get_endpoint_url( 'orders' ) ),
		esc_url( wc_get_endpoint_url( 'edit-address' ) ),
		esc_url( wc_get_endpoint_url( 'edit-account' ) )
	);
	?>
</p>

<p>
	<?php
	printf(
		wp_kses(
			/* translators: %s: contact page url */
			__( 'Every piece is made just for you, so if you ever want to tweak a request, just <a href="%s">say hello</a>.', 'reach-any-stars' ),
			array( 'a' => array( 'href' => array() ) )
		),
		esc_url( home_url( '/contact/' ) )
	);
	?>
</p>

<?php
/**
 * My Account dashboard.
 *
 * @since 2.6.0
 */
do_action( 'woocommerce_account_dashboard' );
