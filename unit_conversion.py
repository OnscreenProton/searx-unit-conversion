'''
searx is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

searx is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with searx. If not, see < http://www.gnu.org/licenses/ >.

(C) 2015 by Adam Tauber, <asciimoo@gmail.com>
(C) 2018, 2020 by Vaclav Zouzalik
'''

from flask_babel import gettext
import re
import pint

name = "Unit Conversion Plugin"
description = gettext("Converts units to different units.")
default_on = True
preference_section = 'query'
query_keywords = ['convert']
query_examples = 'convert 1kg to lbs'

ureg = pint.UnitRegistry()

parser_re = re.compile(r'convert (\d+(?:\.\d+)?)\s?([\w* /^]+) to ([\w* /^]+)', re.I)

def post_search(request, search):
    # Process only on the first page
    if search.search_query.pageno > 1:
        return True

    m = parser_re.match(search.search_query.query)
    if not m:
        # Wrong query format
        return True

    value, source_unit, target_unit = m.groups()

    try:
        # Perform unit conversion using pint
        converted_value = ureg(value + source_unit).to(target_unit).magnitude
        answer = f"{value} {source_unit} is equal to {converted_value} {target_unit}"
    except pint.DimensionalityError:
        answer = "Cannot convert unit"

    # Clear existing results and add the conversion result
    search.result_container.answers.clear()
    search.result_container.answers['unit_conversion'] = {'answer': answer}

    return True

