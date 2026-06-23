// This JavaScript snippet was provided in the official migration documentation. 
// REF: https://canonical-rtd-proxy.readthedocs-hosted.com/how-to/migrate/#overwrite-links-js

// Replace oldDomain with newDomain
const oldDomain = 'canonical-launchpad-documentation.readthedocs-hosted.com';
const newDomain = 'ubuntu.com/docs/launchpad';

// Use a MutationObserver to wait for the RTD flyout element to appear in the DOM
const observer = new MutationObserver(function(mutations, obs) {
    const rtdFlyout = document.querySelector('readthedocs-flyout');
    if (!rtdFlyout) return;

    obs.disconnect();

    rtdFlyout.addEventListener('click', function() {
        const shadowRoot = rtdFlyout.shadowRoot;
        if (!shadowRoot) return;

        const anchors = shadowRoot.querySelectorAll('a');
        anchors.forEach(anchor => {
            anchor.href = anchor.href.replace(new RegExp(oldDomain, 'g'), newDomain);
        });
    });
});

observer.observe(document.body, { childList: true, subtree: true });