# VOIZON Digital Solutions website

Static, multi-page HTML/CSS/JavaScript website for VOIZON Digital Solutions. The site is designed for deployment on GitHub Pages.

## Main pages

- Home, About, Services, Solutions
- International, Our Process, Industries
- Private Project Portfolio, Insights, FAQs
- Contact, Privacy Policy, Terms & Conditions

The Services page links to individual service pages. Keep client names, client materials, project screenshots and results private unless VOIZON has explicit permission to publish them. The public portfolio page is intended to explain the private-sample request process; it is not a login-protected portfolio portal.

## Deploy with GitHub Pages

1. Open **Settings → Pages** in this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**, then save.
4. Wait for the Pages deployment to complete and open the published URL shown in the Pages settings.
5. Test the published site on desktop and mobile, including navigation, page links, forms and WhatsApp actions.

A Git commit alone does not confirm that GitHub Pages is enabled or that the latest version has deployed.

## Pre-launch verification

- Confirm the deployed URL and test the site on real desktop and mobile browsers.
- Compare the recreated SVG logo with the approved VOIZON logo; replace it with the original high-quality asset if it is not an exact match.
- Verify the WhatsApp number and test the enquiry flow on a device with WhatsApp available.
- Confirm the production domain, DNS and HTTPS/SSL settings before publishing a sitemap or final domain-specific metadata.
- Review every service page, navigation link, footer link and call-to-action.
- Confirm that all public claims, service descriptions and any portfolio material are accurate and authorized.
- Replace or confirm the legal business identity and contact details in the Privacy Policy and Terms & Conditions, and obtain an appropriate legal review before relying on them.
- Check that the Privacy Policy accurately describes the tools and data-handling practices actually used by the business.

## Contact form behaviour and limitations

The contact form collects enquiry details in the visitor's browser and opens WhatsApp with a prefilled message addressed to **+91 95674 97943**. The visitor must review and send the message in WhatsApp.

The form does **not** submit to a website backend, save leads in a database, or send an email notification. Do not describe it as a database-backed lead-management system.

## Technical notes

- The website is a static front-end project; it does not currently require a server-side application.
- Shared styling is in `assets/css/style.css`.
- Shared navigation, contact actions and enquiry-form behaviour are in `assets/js/main.js`.
- `robots.txt` is present. Add a production-domain sitemap only after the final domain is confirmed.
