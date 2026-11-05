# Documentation evidence: twilio-webhook-security

Canonical URL: https://www.twilio.com/docs/usage/webhooks/webhooks-security
Retrieved: 2026-11-05
Resolved URL: https://www.twilio.com/docs/usage/webhooks/webhooks-security
Extraction: server-provided Markdown
Version: n/a (living page)

---

---
"@context": https://schema.org
"@type": TechArticle
"@id": https://www.twilio.com/docs/usage/webhooks/webhooks-security#article
headline: Secure webhooks
description: Learn how to secure your web application that uses Twilio webhooks by verifying the sender of the webhook. This guide also covers other common security practices for Twilio webhooks, such as HTTPS and authentication.
url: https://www.twilio.com/docs/usage/webhooks/webhooks-security
inLanguage: en
dateModified: 2026-10-14T20:48:46.000Z
author:
  "@type": Organization
  name: Twilio Developer Education Team
publisher:
  "@type": Organization
  name: Twilio
---

# Secure webhooks

Maintain secure communication between your app and Twilio using encryption and authentication for your [webhooks][webhook].

## Encrypt traffic with HTTPS and TLS

To secure your web app, serve your web app using the *Secure HyperText Transport Protocol* ([HTTPS][]). Twilio won't connect to an HTTPS URL with a self-signed certificate. Use a certificate from a provider such as [Let's Encrypt][].

The Twilio Console always validates SSL certificates.

#### View how to enable SSL cert validation on the Legacy Console

1. Go to **Admin** > **Account Management** > **General Settings** > **General Settings** > [**SSL certificate validation**][lc-ssl-enable].
2. Click **Enabled**.
3. Click **Save**.

## Authenticate with signatures

Twilio signs all HTTP requests to your app with an `X-Twilio-Signature` HTTP header.
Before responding to a webhook request, your web app should check for this HTTP header.

To create this signature, Twilio combines, then hashes, the following data:

* Your account auth token
* The `x-twilio-signature` header value from Twilio
* The Webhook URL set in Twilio
* All request parameters

Twilio hashes the signature with the [HMAC-SHA1][] hashing algorithm using your account auth token as the secret key.

> \[!CAUTION]
>
> The parameters included in webhook events vary by channel and event type and might change in the future.
> Twilio occasionally adds parameters without advance notice.
> Your integration with Twilio webhooks must support evolving parameter sets for signature validation.
> Twilio recommends using the provided signature validation library from a Twilio SDK. Don't implement your own signature validation.

Validate Signature of Request (x-www-form-urlencoded body)

```js
// Get twilio-node from twilio.com/docs/libraries/node
const client = require('twilio');

// Your Auth Token from twilio.com/console
const authToken = process.env.TWILIO_AUTH_TOKEN;

// Store Twilio's request URL (the url of your webhook) as a variable
const url = 'https://mycompany.com/myapp';

// Store the application/x-www-form-urlencoded parameters from Twilio's request as a variable
// In practice, this MUST include all received parameters, not a
// hardcoded list of parameters that you receive today. New parameters
// may be added without notice.
const params = {
  CallSid: 'CA1234567890ABCDE',
  Caller: '+12349013030',
  Digits: '1234',
  From: '+12349013030',
  To: '+18005551212',
};

// Store the X-Twilio-Signature header attached to the request as a variable
const twilioSignature = 'Np1nax6uFoY6qpfT5l9jWwJeit0=';

// Check if the incoming signature is valid for your application URL and the incoming parameters
console.log(client.validateRequest(authToken, twilioSignature, url, params));
```

```py
import os
# Download the twilio-python library from twilio.com/docs/python/install
from twilio.request_validator import RequestValidator

# Your Auth Token from twilio.com/user/account
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Initialize the request validator
validator = RequestValidator(auth_token)

# Store Twilio's request URL (the url of your webhook) as a variable
url = 'https://example.com/myapp'

# Store the application/x-www-form-urlencoded parameters from Twilio's request as a variable
# In practice, this MUST include all received parameters, not a
# hardcoded list of parameters that you receive today. New parameters
# may be added without notice.
params = {
  'CallSid': 'CA1234567890ABCDE',
  'Caller': '+12349013030',
  'Digits': '1234',
  'From': '+12349013030',
  'To': '+18005551212'
}

# Store the X-Twilio-Signature header attached to the request as a variable
twilio_signature = 'Np1nax6uFoY6qpfT5l9jWwJeit0='

# Check if the incoming signature is valid for your application URL and the incoming parameters
print(validator.validate(url, params, twilio_signature))
```

```cs
// Download the twilio-csharp library from
// https://www.twilio.com/docs/libraries/csharp#installation
using System;
using System.Collections.Generic;
using Twilio.Security;

class Example
{
    static void Main(string[] args)
    {
        // Your Auth Token from twilio.com/console
        const string authToken = Environment.GetEnvironmentVariable("TWILIO_AUTH_TOKEN");

        // Initialize the request validator
        var validator = new RequestValidator(authToken);

        // Store Twilio's request URL (the url of your webhook) as a variable
        const string url = "https://example.com/myapp";

        // Store the application/x-www-form-urlencoded params from Twilio's request as a variable
        // In practice, this MUST include all received parameters, not a
        // hardcoded list of parameters that you receive today. New parameters
        // may be added without notice.
        var parameters = new Dictionary<string, string>
        {
            {"CallSid", "CA1234567890ABCDE"},
            {"Caller", "+12349013030"},
            {"Digits", "1234"},
            {"From", "+12349013030"},
            {"To", "+18005551212"}
        };

        // Store the X-Twilio-Signature header attached to the request as a variable
        const string twilioSignature = "Np1nax6uFoY6qpfT5l9jWwJeit0=";

        // Check if the incoming signature is valid for your application URL and the incoming parameters
        Console.WriteLine(validator.Validate(url, parameters, twilioSignature));
    }
}
```

```java
// Install the Java helper library from twilio.com/docs/java/install
import java.util.HashMap;
import java.util.Map;

import com.twilio.security.RequestValidator;

public class Example {
  // Your Auth Token from twilio.com/user/account
  public static final String AUTH_TOKEN = System.getenv("TWILIO_AUTH_TOKEN");
    
  public static void main(String[] args) throws java.net.URISyntaxException {
    // Initialize the request validator
    RequestValidator validator = new RequestValidator(AUTH_TOKEN);

    // Store Twilio's request URL (the url of your webhook) as a variable
    String url = "https://example.com/myapp";

    // Store the application/x-www-form-urlencoded parameters from Twilio's request as a variable
    // In practice, this MUST include all received parameters, not a
    // hardcoded list of parameters that you receive today. New parameters
    // may be added without notice.
    Map<String, String> params = new HashMap<>();
    params.put("CallSid", "CA1234567890ABCDE");
    params.put("Caller", "+12349013030");
    params.put("Digits", "1234");
    params.put("From", "+12349013030");
    params.put("To", "+18005551212");

    // Store the X-Twilio-Signature header attached to the request as a variable
    String twilioSignature = "Np1nax6uFoY6qpfT5l9jWwJeit0=";

    // Check if the incoming signature is valid for your application URL and the incoming parameters
    System.out.println(validator.validate(url, params, twilioSignature));
  }
}
```

```go
package main

import (
	"fmt"
	"os"

	"github.com/twilio/twilio-go/client"
)

func main() {
	// Your Auth Token from twilio.com/console
	authToken := os.Getenv("TWILIO_AUTH_TOKEN")

	// Initialize the request validator
	requestValidator := client.NewRequestValidator(authToken)

	// Store Twilio's request URL (the url of your webhook) as a variable
	url := "https://example.com/myapp"

	// Store the application/x-www-form-urlencoded params from Twilio's request as a variable
	// In practice, this MUST include all received parameters, not a
	// hardcoded list of parameters that you receive today. New parameters
	// may be added without notice.
	params := map[string]string{
		"CallSid": "CA1234567890ABCDE",
		"Caller":  "+12349013030",
		"Digits":  "1234",
		"From":    "+12349013030",
		"To":      "+18005551212",
	}

	// Store the X-Twilio-Signature header attached to the request as a variable
	signature := "Np1nax6uFoY6qpfT5l9jWwJeit0="

	// Check if the incoming signature is valid for your application URL and the incoming parameters
	fmt.Println(requestValidator.Validate(url, params, signature))
}
```

```php
<?php
// NOTE: This example uses the next generation Twilio helper library - for more
// information on how to download and install this version, visit
// https://www.twilio.com/docs/libraries/php
require_once '/path/to/vendor/autoload.php';

use Twilio\Security\RequestValidator;

// Your auth token from twilio.com/user/account
$token = getenv("TWILIO_AUTH_TOKEN");

// The X-Twilio-Signature header - in PHP this should be
// You may be able to use $signature = $_SERVER["HTTP_X_TWILIO_SIGNATURE"];
$signature = 'Np1nax6uFoY6qpfT5l9jWwJeit0=';

// Initialize the request validator
$validator = new RequestValidator($token);

// The Twilio request URL. You may be able to retrieve this from
// You may be able to use $url = $_SERVER['SCRIPT_URI']
$url = 'https://example.com/myapp';

// Store the application/x-www-form-urlencoded parameters from Twilio's request as a variable
// In practice, this MUST include all received parameters, not a
// hardcoded list of parameters that you receive today. New parameters
// may be added without notice.
// You may be able to use $postVars = $_POST
$postVars = array(
  'CallSid' => 'CA1234567890ABCDE',
  'Caller' => '+12349013030',
  'Digits' => '1234',
  'From' => '+12349013030',
  'To' => '+18005551212'
);

// Check if the incoming signature is valid for your application URL and the incoming parameters
if ($validator->validate($signature, $url, $postVars)) {
  echo "Confirmed to have come from Twilio.";
} else {
  echo "NOT VALID. It might have been spoofed!";
}
```

```rb
# Get twilio-ruby from twilio.com/docs/ruby/install
require 'rubygems' # This line not needed for ruby > 1.8
require 'twilio-ruby'

# Get your Auth Token from https://www.twilio.com/console
auth_token = ENV['TWILIO_AUTH_TOKEN']

#  Initialize the request validator
validator = Twilio::Security::RequestValidator.new(auth_token)

# Store Twilio's request URL (the url of your webhook) as a variable
url = 'https://example.com/myapp'

# Store the application/x-www-form-urlencoded params from Twilio's request as a variable
# In practice, this MUST include all received parameters, not a
# hardcoded list of parameters that you receive today. New parameters
# may be added without notice.
params = {
  'CallSid' => 'CA1234567890ABCDE',
  'Caller'  => '+12349013030',
  'Digits'  => '1234',
  'From'    => '+12349013030',
  'To'      => '+18005551212'
}

# Store the X-Twilio-Signature header attached to the request as a variable
twilio_signature = 'Np1nax6uFoY6qpfT5l9jWwJeit0='

# Check if the incoming signature is valid for your application URL and the incoming parameters
puts validator.validate(url, params, twilio_signature)
```

Validate Signature of Request (application/json body)

```js
// Get twilio-node from twilio.com/docs/libraries/node
const client = require('twilio');

// Your Auth Token from twilio.com/console
const authToken = process.env.TWILIO_AUTH_TOKEN;

// Store Twilio's request URL (the url of your webhook) as a variable
// including all query parameters
const url =
  'https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9';

// Store the application/json body from Twilio's request as a variable
// In practice, this MUST include all received parameters, not a
// hardcoded list of parameters that you receive today. New parameters
// may be added without notice.
const body = '{"CallSid":"CA1234567890ABCDE","Caller":"+12349013030"}';

// Store the X-Twilio-Signature header attached to the request as a variable
const twilioSignature = 'hqeF3G9Hrnv6/R0jOhoYDD2PPUs=';

// Check if the incoming signature is valid for your application URL and the incoming body
console.log(
  client.validateRequestWithBody(authToken, twilioSignature, url, body)
);
```

```py
import os
# Download the twilio-python library from twilio.com/docs/python/install
from twilio.request_validator import RequestValidator

# Your Auth Token from twilio.com/user/account
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Initialize the request validator
validator = RequestValidator(auth_token)

# Store Twilio's request URL (the url of your webhook) as a variable
# including all query parameters
url = 'https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9'

# Store the application/json body from Twilio's request as a variable
# In practice, this MUST include all received parameters, not a
# hardcoded list of parameters that you receive today. New parameters
# may be added without notice.
body = """{"CallSid":"CA1234567890ABCDE","Caller":"+12349013030"}"""

# Store the X-Twilio-Signature header attached to the request as a variable
twilio_signature = 'hqeF3G9Hrnv6/R0jOhoYDD2PPUs='

# Check if the incoming signature is valid for your application URL and the incoming body
print(validator.validate(url, body, twilio_signature))
```

```cs
// Download the twilio-csharp library from
// https://www.twilio.com/docs/libraries/csharp#installation
using System;
using System.Collections.Generic;
using Twilio.Security;

class Example
{
    static void Main(string[] args)
    {
        // Your Auth Token from twilio.com/console
        const string authToken = Environment.GetEnvironmentVariable("TWILIO_AUTH_TOKEN");

        // Initialize the request validator
        var validator = new RequestValidator(authToken);

        // Store Twilio's request URL (the url of your webhook) as a variable
        // including all query parameters
        const string url = "https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9";

        // Store the application/json body from Twilio's request as a variable
        // In practice, this MUST include all received parameters, not a
        // hardcoded list of parameters that you receive today. New parameters
        // may be added without notice.
        const string body = "{\"CallSid\":\"CA1234567890ABCDE\",\"Caller\":\"+12349013030\"}";


        // Store the X-Twilio-Signature header attached to the request as a variable
        const string twilioSignature = "hqeF3G9Hrnv6/R0jOhoYDD2PPUs=";

        // Check if the incoming signature is valid for your application URL and the incoming body
        Console.WriteLine(validator.Validate(url, body, twilioSignature));
    }
}
```

```java
// Install the Java helper library from twilio.com/docs/java/install
import com.twilio.security.RequestValidator;

public class Example {
  // Your Auth Token from twilio.com/user/account
  public static final String AUTH_TOKEN = System.getenv("TWILIO_AUTH_TOKEN");

  public static void main(String[] args) throws java.net.URISyntaxException {
    // Initialize the request validator
    RequestValidator validator = new RequestValidator(AUTH_TOKEN);

    // Store Twilio's request URL (the url of your webhook) as a variable
    // including all query parameters
    String url = "https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9";

    // Store the application/json body from Twilio's request as a variable
    // In practice, this MUST include all received parameters, not a
    // hardcoded list of parameters that you receive today. New parameters
    // may be added without notice.
    String body = "{\"CallSid\":\"CA1234567890ABCDE\",\"Caller\":\"+12349013030\"}";

    // Store the X-Twilio-Signature header attached to the request as a variable
    String twilioSignature = "hqeF3G9Hrnv6/R0jOhoYDD2PPUs=";

    // Check if the incoming signature is valid for your application URL and the incoming body
    System.out.println(validator.validate(url, body, twilioSignature));
  }
}
```

```go
package main

import (
	"fmt"
	"os"

	"github.com/twilio/twilio-go/client"
)

func main() {
	// Your Auth Token from twilio.com/console
	authToken := os.Getenv("TWILIO_AUTH_TOKEN")

	// Initialize the request validator
	requestValidator := client.NewRequestValidator(authToken)

	// Store Twilio's request URL (the url of your webhook) as a variable
	// including all query parameters
	url := "https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9"

	// Store the application/json body from Twilio's request as a variable
	// In practice, this MUST include all received parameters, not a
	// hardcoded list of parameters that you receive today. New parameters
	// may be added without notice.
	body :=  []byte("{\"CallSid\":\"CA1234567890ABCDE\",\"Caller\":\"+12349013030\"}")

	// Store the X-Twilio-Signature header attached to the request as a variable
	signature := "hqeF3G9Hrnv6/R0jOhoYDD2PPUs="

	// Check if the incoming signature is valid for your application URL and the incoming parameters
	fmt.Println(requestValidator.ValidateBody(url, body, signature))
}
```

```php
<?php
// NOTE: This example uses the next generation Twilio helper library - for more
// information on how to download and install this version, visit
// https://www.twilio.com/docs/libraries/php
require_once '/path/to/vendor/autoload.php';

use Twilio\Security\RequestValidator;

// Your auth token from twilio.com/user/account
$token = getenv("TWILIO_AUTH_TOKEN");

// The X-Twilio-Signature header - in PHP this should be
// You may be able to use $signature = $_SERVER["HTTP_X_TWILIO_SIGNATURE"];
$signature = 'hqeF3G9Hrnv6/R0jOhoYDD2PPUs=';

// Initialize the request validator
$validator = new RequestValidator($token);

// Store Twilio's request URL (the url of your webhook) as a variable
// including all query parameters
// You may be able to use $url = $_SERVER['SCRIPT_URI']
$url = 'https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9';

// Store the application/json body from Twilio's request as a variable
// In practice, this MUST include all received parameters, not a
// hardcoded list of parameters that you receive today. New parameters
// may be added without notice.
// You may be able to use $body = $_POST
$body = "{\"CallSid\":\"CA1234567890ABCDE\",\"Caller\":\"+12349013030\"}";

// Check if the incoming signature is valid for your application URL and the incoming parameters
if ($validator->validate($signature, $url, $body)) {
  echo "Confirmed to have come from Twilio.";
} else {
  echo "NOT VALID. It might have been spoofed!";
}
```

```rb
# Get twilio-ruby from twilio.com/docs/ruby/install
require 'rubygems' # This line not needed for ruby > 1.8
require 'twilio-ruby'

# Get your Auth Token from https://www.twilio.com/console
auth_token = ENV['TWILIO_AUTH_TOKEN']

#  Initialize the request validator
validator = Twilio::Security::RequestValidator.new(auth_token)

# Store Twilio's request URL (the url of your webhook) as a variable
url = 'https://example.com/myapp?bodySHA256=5ccde7145dfb8f56479710896586cb9d5911809d83afbe34627818790db0aec9'

# Store the application/json body from Twilio's request as a variable
# In practice, this MUST include all received parameters, not a
# hardcoded list of parameters that you receive today. New parameters
# may be added without notice.
body = '{"CallSid":"CA1234567890ABCDE","Caller":"+12349013030"}'

# Store the X-Twilio-Signature header attached to the request as a variable
twilio_signature = 'hqeF3G9Hrnv6/R0jOhoYDD2PPUs='

# Check if the incoming signature is valid for your application URL and the incoming body
puts validator.validate(url, body, twilio_signature)
```

To learn more about how Twilio signs requests to your app, see [Validating Requests][valid-sigs].

### Understand parameters in signature validation

Twilio webhooks deliver data to your app based on the content type of the request.
To validate webhook signatures, prepare to ingest all three parameter types: query, form, and body.

#### Query parameters

Query parameters appear in the webhook URL after the `?` character.

For example: The URL `https://example.com/webhook?foo=1&bar=2` contains two query parameters: `foo` and `bar`.

As query parameters comprise part of the full URL, they get passed your validation function URL. Never extract query parameters and pass them separately to the function's `params` argument.

When making a webhook request, use the exact URL from Twilio including any [URL-encoded characters][URL encoding]. If you decode or re-encode the URL, signature validation fails.

#### Form parameters

The `POST` request body includes form parameters using the [content-type][] `application/x-www-form-urlencoded`. These parameters include webhook-specific fields such as `CallSid`, `From`, `To`, and `Body`.

Extract the form parameters from the request body and pass them to the validation function as a collection of name and value pairs, such as a dictionary or hash map. Twilio sorts these parameters alphabetically and appends them to the URL when calculating the signature. For a working example in your language, see the [signature validation code samples][].

#### JSON request bodies

Twilio can also send JSON payloads with the content type `application/json`. For these requests, Twilio appends a `bodySHA256` query parameter to your webhook URL. The parameter value is a SHA-256 hash of the raw JSON request body.

When validating JSON webhooks:

* Don't extract individual JSON properties or treat them as form parameters.
* Use your SDK's JSON-specific validation method (for example, `validateRequestWithBody`) and pass the raw request body string.

The SDK performs two checks:

1. It verifies that the SHA-256 hash of the raw body matches the `bodySHA256` query parameter.
2. It validates the request signature by including the `bodySHA256` value during the calculation.

## Tutorials for validating incoming Twilio requests

To add Twilio request validation to your app, follow one of the following tutorials for your preferred language and framework.

* [Node.js / Express][]
* [C# / ASP.NET Core][]
* [C# / ASP.NET][]
* [C# / ASP.NET WEB API][]
* [Java / Servlets][]
* [Python / Django][]
* [Python / Flask][]
* [Python / Amazon Web Services Lambda][valid-sigs]
* [PHP / Lumen][]
* [Ruby / Sinatra][]
* [Go / Gin][]

## Webhooks and IP addresses

Twilio provides services through cloud architecture. This results in Twilio not having a fixed range of IP addresses that issue webhooks.

When designing your network architecture, you may want to have one set of servers and a load balancer in a DMZ that receive webhook requests from Twilio. You can then proxy those requests to your private network.

To learn more about Twilio and IP addresses, see [All About Twilio IP Addresses][].

## HTTP authentication

Twilio supports HTTP Basic and Digest Authentication. This allows you to password-protect the TwiML URLs on your web server so that only you and Twilio can access them. You may provide a username and password via the following URL format.

```bash
https://username:password@www.myserver.com/my_secure_document
```

> \[!NOTE]
>
> Twilio continues to support credentials in the URL, but recommends that you use the [Webhooks configuration API][config] to configure webhook delivery. To move an endpoint over, see [Migrate to the Webhooks configuration API][migrate].

To learn more about how Twilio uses HTTP authentication for webhook requests, see the [Security][] guide.

[config]: /docs/usage/webhooks/webhook-configuration

[migrate]: /docs/usage/webhooks/webhook-migration

[All About Twilio IP Addresses]: https://help.twilio.com/hc/en-us/articles/115015934048-All-About-Twilio-IP-Addresses

[C# / ASP.NET Core]: /docs/usage/tutorials/how-to-secure-your-csharp-aspnet-core-app-by-validating-incoming-twilio-requests

[C# / ASP.NET WEB API]: /docs/usage/tutorials/how-to-secure-your-csharp-aspnet-web-api-app-by-validating-incoming-twilio-requests

[C# / ASP.NET]: /docs/usage/tutorials/how-to-secure-your-csharp-aspnet-app-by-validating-incoming-twilio-requests

[Go / Gin]: /docs/usage/tutorials/how-to-secure-your-gin-project-by-validating-incoming-twilio-requests

[Java / Servlets]: /docs/usage/tutorials/how-to-secure-your-servlet-app-by-validating-incoming-twilio-requests

[Let's Encrypt]: https://letsencrypt.org

[Node.js / Express]: /docs/usage/tutorials/how-to-secure-your-express-app-by-validating-incoming-twilio-requests

[PHP / Lumen]: /docs/usage/tutorials/how-to-secure-your-lumen-app-by-validating-incoming-twilio-requests

[valid-sigs]: /docs/usage/security#validating-requests

[Python / Django]: /docs/usage/tutorials/how-to-secure-your-django-project-by-validating-incoming-twilio-requests

[Python / Flask]: /docs/usage/tutorials/how-to-secure-your-flask-app-by-validating-incoming-twilio-requests

[Ruby / Sinatra]: https://www.twilio.com/blog/secure-your-sinatra-app-validating-incoming-twilio-requests

[Security]: /docs/usage/security#http-authentication

[lc-ssl-enable]: https://console.twilio.com/us1/account/manage-account/general-settings

[URL encoding]: https://en.wikipedia.org/wiki/Percent-encoding

[content-type]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type

[HMAC-SHA1]: /docs/usage/security#a-note-on-hmac-sha1

[webhook]: /docs/glossary/what-is-a-webhook

[https]: https://en.wikipedia.org/wiki/HTTPS

[signature validation code samples]: #authenticate-with-signatures

