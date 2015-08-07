from django.conf.urls import patterns, url

# We adjust the regular expression for our URL to include a capture group, (.+),
# which will match any characters, up to the following /. The captured text will
# get passed to the view as an argument.
# In other words, if we go to the URL /lists/1/, view_list will get a second argument
#  after the normal request argument, namely the string "1". If we go to /lists/foo/,
# we get view_list(request, "foo").
# (.+) is a greedy regex. We can fix that by making our URL pattern explicitly capture
# only numerical digits, by using the regular expression \d:
urlpatterns = patterns('',
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
)
