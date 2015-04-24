# -*- coding: utf-8 -*-

# Copyright © 2012-2015 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola.plugin_categories import RestExtension

class Plugin(RestExtension):

    name = "rest_advert"

    def set_site(self, site):
        self.site = site
        directives.register_directive('advert', Advert)
        return super(Plugin, self).set_site(site)


class Advert(Directive):
    """ Restructured text extension for inserting Google Adsense advert.

    Usage: .. advert:: advert-type

    Currently advert-type is blog-responsive-sidebar or blog-responsive-banner
    and the result is one fixed chunk of HTML or another one.
    """
    required_arguments = 1
    optional_arguments = 0
    has_content = False

    def run(self):
        if self.arguments[0] == "blog-responsive-sidebar":
            return [nodes.raw('', """<div class="blog-ad-container-skyscraper">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- blog responsive sidebar -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1959826171259933"
     data-ad-slot="9751446737"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>""", format='html')]
        else:
            return [nodes.raw('', """<div class="blog-ad-container-banner">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- blog responsive banner -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1959826171259933"
     data-ad-slot="8774241139"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>""", format='html')]
