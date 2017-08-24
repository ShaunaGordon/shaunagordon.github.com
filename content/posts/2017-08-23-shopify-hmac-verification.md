title: Shopify HMAC Verification
subtitle: The Right Way
date: 2017-08-23 20:30
category: tech
tags: shopify, oauth, php

[TOC]

I get the pleasure of writing integration after integration to Shopify at my day job. As a result, I have become quite familiar with their documentation and its gaps. The HMAC verification piece of the OAuth/embedded app installation process is a particularly glaring gap. So let's close it.

# What's Wrong With The Docs?

If you're a Ruby developer, probably not much. Shopify's got a nice little Ruby gem that does a great deal of the work for you. Happy days!

But for a PHP developer like myself? Well...[the docs look pretty much like this](https://help.shopify.com/api/sdks/shopify-apps/embedded-app-sdk/getting-started):

1. Create an app in the dashboard
1. Add the redirect code
1. ????
1. Profit!

What's even worse, is that one of the [few libraries](https://github.com/joshrps/laravel-shopify-API-wrapper) *and* [step-by-step PHP examples](https://www.shopify.com/partners/blog/17056443-how-to-generate-a-shopify-api-token) are both **wrong** in how they do HMAC verification! (The fact that that guide is on Shopify, proper, is astounding to me.)

Okay, so that entire section is in dire need of a *good* tutorial for those not blessed with Ruby. I'll get to that in the near future. In the meantime, I want to have out there the *correct* way of doing HMAC verification.

# The *Right* Way

The documentation does actually give us [the information on how to correctly generate the HMAC value,](https://help.shopify.com/api/getting-started/authentication/oauth#verification) but it does so in a language-agnostic way (which is all well and good, but requires quite a bit of fiddling to get it right).

They can be summarized as follows:

1. Pull everything from the request *except* the HMAC and signature fields
1. Sort remaining items lexilogically
1. Replace special characters in keys and values
1. Hash per HMAC standards with the shared secret (query string, SHA256)

If done properly, the generate string should match the HMAC field Shopify sent.

Now, what's that look like in PHP? Pretty simple, thankfully:

<script src="https://gist.github.com/ShaunaGordon/24da74ac66d0d2d8259fe52df0f57ef3.js?file=hmac_vanilla.php"></script>

If you happen to be running Laravel, you can clean it up a little, like this:

<script src="https://gist.github.com/ShaunaGordon/24da74ac66d0d2d8259fe52df0f57ef3.js?file=hmac_laravel.php"></script>

How does this differ from the other ways? For the most part, the fatal error in the available examples is that they do step 1 (of all things) *backwards*. Instead of taking the request and *removing* the keys that need removed, they all *built* an array from the keys in the example code in the documentation. This was all well and good while the response from Shopify matched the documentation, but as soon as they changed that response, well...everything broke.

But, now you have it! The right way to do Shopify's HMAC verification. In the near future, I'll be writing up a tutorial on how to painlessly set up a Shopify embedded app in PHP.
