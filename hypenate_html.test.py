"""
Test for hyphenate_html

Author: Craig Weber
"""

import hyphenate_html as hyphen
import re
from lib.BeautifulSoup import BeautifulSoup, NavigableString

lipsum = """<div><p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin tincidunt nibh nec ipsum molestie a semper augue consequat. Suspendisse sollicitudin lectus eget justo scelerisque feugiat. Quisque dapibus consectetur ante at imperdiet. In aliquet augue nisl, in fermentum nibh. Etiam vehicula, est eu scelerisque convallis, nibh massa varius dui, ut interdum sem augue et sem. Nunc accumsan facilisis est ut bibendum. Ut sed consectetur leo. Sed vel nisi mauris. Cras turpis est, molestie at bibendum id, ullamcorper sed justo. Curabitur sem odio, volutpat non blandit sit amet, venenatis sit amet odio. Donec molestie vehicula lacus, at convallis nulla ornare eget. Ut nisi velit, luctus at rutrum vel, dapibus vel mauris. Morbi accumsan urna eget justo tincidunt blandit id at neque. Aliquam ut purus elit, et tempor lectus.
</p>
<p>
Nam ac elit nisl. Cras ac leo a risus fringilla mollis id a quam. Etiam vitae dui arcu, ac congue nisi. Mauris vel velit quam, at mattis turpis. Curabitur consequat convallis diam tempus aliquam. Aliquam posuere, nulla in molestie placerat, justo nisl condimentum mauris, non ultrices elit arcu nec tellus. Integer eget consectetur tellus. Nullam sodales nulla a tellus auctor dignissim. Nam laoreet quam non mi pulvinar gravida. Praesent nec lorem nisl, at ultrices lacus. Maecenas dapibus, purus vitae molestie placerat, metus risus egestas sem, ac volutpat orci erat eu ligula.
</p>
<p>
Suspendisse potenti. Nullam commodo lectus a odio dapibus sollicitudin. Aenean consequat, diam in tincidunt varius, sem odio ornare magna, vel rutrum nisi velit eu orci. Sed porta ultricies fermentum. Aliquam et interdum sem. Etiam vestibulum sagittis mattis. Nunc tincidunt viverra lorem nec convallis. Sed commodo convallis ligula. Nulla vel libero dolor, sit amet lobortis ligula. In posuere nisl nec velit viverra sollicitudin. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris a felis et lacus euismod laoreet in a urna. In hac habitasse platea dictumst. Curabitur scelerisque mattis arcu, vel adipiscing lacus auctor sed. Suspendisse potenti.
</p>
<p>
Nullam tempus metus sit amet leo ultrices quis bibendum nisi ultrices. Praesent et magna in mi ultrices pulvinar. Suspendisse pharetra, dui eu viverra pharetra, quam velit rhoncus neque, nec hendrerit leo ipsum non est. Sed a arcu ac libero congue eleifend nec et felis. Suspendisse aliquet elementum ligula at tempor. Donec vel mi commodo justo viverra blandit. Curabitur purus erat, accumsan vel laoreet a, rhoncus at diam. Etiam adipiscing varius lacus, eget sagittis justo dignissim ac. Curabitur at ullamcorper risus. Donec adipiscing nulla eu enim faucibus facilisis. Duis ornare posuere felis, sit amet accumsan tellus tempus sed. Ut arcu urna, iaculis at pretium a, suscipit eu libero. Pellentesque dolor est, varius ac egestas egestas, vestibulum eu nibh. Phasellus sed nunc risus. Aliquam tortor enim, blandit ac feugiat nec, sagittis at nibh. Etiam nec est nec urna sagittis vestibulum eget vitae turpis. Cras nisl neque, volutpat tincidunt aliquam ac, interdum vitae arcu. Ut id libero id sem vestibulum vehicula. Curabitur id justo diam.
</p>
<p>
Aenean id metus et nunc tincidunt facilisis. Donec sodales, sem vitae malesuada commodo, ligula dolor condimentum lectus, eget scelerisque elit lacus fermentum diam. Nulla faucibus orci id massa porta gravida. Nam nunc tortor, ultrices eu aliquet eu, mollis sed velit. Pellentesque varius porttitor malesuada. Proin quis turpis nisl, in lobortis nisl. Sed imperdiet pulvinar malesuada. Curabitur tristique neque sit amet elit porttitor sed iaculis odio scelerisque. Donec tincidunt varius consectetur. Vivamus mollis consectetur scelerisque. Nullam blandit arcu eu nunc hendrerit convallis. Sed facilisis varius arcu, condimentum sodales nunc suscipit sed. Vestibulum a turpis ligula. In hac habitasse platea dictumst. Phasellus porttitor eleifend nisl et porttitor. Aenean accumsan placerat condimentum. Sed semper tincidunt aliquet. Pellentesque tempor enim gravida odio bibendum auctor. Duis vel velit quis lorem pretium porttitor.
</p>
<p>
Nullam vulputate dictum turpis nec fringilla. Integer eu ultricies nisi. Mauris feugiat mauris eget ligula aliquam scelerisque pretium felis cursus. Quisque semper dapibus libero sit amet tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Suspendisse malesuada suscipit sagittis. Maecenas justo ante, commodo in posuere eget, vulputate quis eros. Phasellus eros augue, bibendum nec varius at, sodales suscipit elit. Vivamus non tellus eu dolor faucibus laoreet vitae at mi. Aliquam diam nibh, pulvinar sed fringilla quis, volutpat ut est.
</p>
<p>
In elit libero, fringilla sed tincidunt sit amet, elementum in leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce adipiscing consequat neque, nec posuere lectus ullamcorper nec. Nullam est orci, hendrerit eget hendrerit ac, adipiscing nec lacus. Sed diam lorem, interdum non aliquet nec, convallis non dui. Sed sagittis eleifend pretium. Etiam libero velit, varius eu mollis quis, mattis at nisl. Morbi ultrices, nulla eget imperdiet mattis, felis eros accumsan neque, et imperdiet erat metus eget nunc. Nam hendrerit magna sit amet orci egestas sed interdum elit pretium. Nullam a urna vel mauris ullamcorper suscipit.
</p>
<p>
<pre>Hey now</pre>
Sed congue, nunc sit amet imperdiet dignissim, nisl sapien pulvinar libero, non eleifend enim urna vitae quam. Integer adipiscing lectus ac elit ornare commodo. Suspendisse potenti. Aliquam consectetur tellus vitae nibh sagittis molestie. Mauris nec nibh et ligula commodo tempor. Nunc sit amet tellus erat. Quisque risus purus, egestas a rutrum et, vulputate id justo. Donec varius gravida turpis, vel placerat mi viverra ac. Phasellus dapibus cursus velit, at accumsan orci convallis id. Donec ut mi dui.
</p>
<p>
Suspendisse tempor ultricies turpis quis volutpat. Pellentesque congue metus sit amet dui lacinia blandit quis sit amet lacus. Etiam convallis tincidunt libero, a malesuada eros egestas feugiat. Sed arcu nunc, commodo at porttitor eget, viverra nec nibh. Morbi porta mollis leo, at gravida erat feugiat id. Fusce sit amet facilisis quam. Mauris id velit sem. Sed arcu neque, adipiscing cursus posuere tempor, iaculis vel nisi. Nunc ut erat orci. Nullam pharetra sollicitudin augue. Curabitur sit amet blandit dui. Phasellus eros lectus, commodo sed gravida eu, vestibulum sed orci. Aenean vel fringilla lacus. Donec dapibus feugiat augue eget rhoncus. Donec quis est mollis risus ultrices varius et at nunc. Vestibulum pharetra accumsan nunc, aliquet volutpat turpis pellentesque ut.
</p>
<div><p>Hiya<code>Code shouldn't be replaced.</code></p></div>
<p>
Curabitur ut est lacus, vel condimentum ipsum. Curabitur vulputate sapien at nisi posuere volutpat. Ut ullamcorper lacinia lacus nec suscipit. In sit amet risus quis erat rutrum ultricies. Aenean id orci et purus mollis condimentum eget vel lacus. Vivamus vestibulum libero id dui pharetra accumsan. Fusce eros erat, vehicula vitae dictum eu, fringilla vitae neque. Vivamus ac ipsum ipsum, et fringilla orci. Sed ac facilisis quam. Ut tellus lorem, vestibulum sed tempus non, consequat a dui. Nulla facilisi. Nam fringilla eleifend ultricies. In hac habitasse platea dictumst. Quisque auctor blandit rhoncus. Praesent tempor dolor in quam volutpat posuere.
</p></div><div></div>"""


            
print hyphen.hyphenate_html(lipsum)





