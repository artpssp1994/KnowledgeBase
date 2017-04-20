from cis import settings
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.template.defaultfilters import filesizeformat
from knowledge_management.forms import CategoryForm, PageForm, CommentForm, LikeCommentForm
from knowledge_management.models import Super_category, Comment, LikeComment, LikePage
from tagging.models import Tag, TaggedItem
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from knowledge_management.models import Document
from knowledge_management.forms import DocumentForm



# Create your views here.

from knowledge_management.models import Category, Page
from django.http import HttpResponse

def showtopic(request):
    context_dict = {}
    category_list = Category.objects.order_by('name')
    context_dict['categories'] = category_list
    pages = Page.objects.order_by('title')
    context_dict['pages'] = pages
    return render(request, 'knowledge_management/show_topic.html', context_dict)

def search(request):

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.views = 0
            page.postby = request.user
            page.save()
            # probably better to use a redirect here.
            return recentpost(request)
        else:
            print(form.errors)
    else:
        form = PageForm()

    context_dict = {'form':form,}
    category_list = Category.objects.order_by('name')
    context_dict['categories'] = category_list
    tags = Tag.objects.order_by('name')
    array = []
    for run in range(len(tags)):
        x = str(tags[run])
        array.append(x)

    context_dict['tags'] = tags

    return render(request, 'knowledge_management/search.html', context_dict)

def recentpost(request):
    context_dict = {}
    sup_category = Super_category.objects.order_by('name')
    context_dict['sup_category'] = sup_category
    category_list = Category.objects.order_by('name')
    context_dict['categories'] = category_list
    pages = Page.objects.order_by('-date')[:10]
    context_dict['pages'] = pages
    array = {}
    for runall in pages:
        count_page = Comment.objects.filter(page = runall).count()
        array[runall] = count_page

    context_dict['array'] = array
    return render(request, 'knowledge_management/recentpost.html', context_dict)

def sub_category(request, category_name_slug, supcategory_name_slug, page):
    context_dict = {}
    try:
        x = (int(page)*20) - 20
        sup_category = Super_category.objects.get(id=supcategory_name_slug)
        context_dict['sup_category'] = sup_category
        context_dict['supcategory_name_slug'] =sup_category.name
        category_zero_slug = category_name_slug
        context_dict['category_zero_slug'] =category_zero_slug
        redirect = Category.objects.filter(super_category=sup_category)[:1]
        context_dict['redirect'] = redirect
        category_list = Category.objects.filter(super_category=sup_category)
        context_dict['categories'] = category_list
        category_target = Category.objects.get(id=category_name_slug)
        context_dict['category_target'] = category_target

        divide = Page.objects.filter(category=category_target)
        if int(divide.count()%20) > 0 :
            carry = 1
        else:
            carry = 0
        numpage = range(1, (int(divide.count()/20)+carry)+1)
        context_dict['numpage'] = numpage
        pages = Page.objects.filter(category=category_target).order_by('-date')[x:x+20]
        context_dict['pages'] = pages

        array = {}
        for runall in pages:
            count_page = Comment.objects.filter(page = runall).count()
            array[runall] = count_page

        context_dict['array'] = array

    except Category.DoesNotExist:
        pass
    return render(request, 'knowledge_management/sub_category.html', context_dict)

def topknowledge(request):
    context_dict = {}
    sup_category = Super_category.objects.order_by('name')
    context_dict['sup_category'] = sup_category
    category_list = Category.objects.order_by('name')
    context_dict['categories'] = category_list
    pages = Page.objects.order_by('-like')[:50]
    context_dict['pages'] = pages
    array = {}
    for runall in pages:
        count_page = Comment.objects.filter(page = runall).count()
        array[runall] = count_page

    context_dict['array'] = array

    return render(request, 'knowledge_management/topknowledge.html', context_dict)

def category(request):
    context_dict = {}
    try:
        sup_category = Super_category.objects.order_by('name')
        context_dict['sup_category'] = sup_category
        categories = Category.objects.filter(super_category= sup_category)[:1]
        context_dict['categories'] = categories

        array = {}
        for runall in sup_category:
            count_page = 0
            sub_category = Category.objects.filter(super_category= runall)
            for runsc in sub_category:
                count_page += Page.objects.filter(category= runsc).count()
            array[runall] = count_page
        context_dict['array'] = array

    except Category.DoesNotExist:
        pass
    return render(request, 'knowledge_management/category.html', context_dict)

def page(request, category_name_slug, page_name_slug, supcategory_name_slug):
    #return render(request, 'knowledge_management/'+supcategory_name_slug+'/' )
    context_dict = {}
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            page = Page.objects.get(id=page_name_slug)
            c = form.save(commit=False)
            c.page = page
            c.postby = request.user
            #c.like = 0
            c.save()
            url = reverse('knowledge_management.views.page', kwargs={'category_name_slug': category_name_slug, 'page_name_slug': page_name_slug,'supcategory_name_slug': supcategory_name_slug })
            return HttpResponseRedirect(url)
    else:
        form = CommentForm()

    context_dict['form'] = form

    try:
        sup_category = Super_category.objects.get(id=supcategory_name_slug)
        context_dict['sup_category'] = sup_category
        context_dict['supcategory_name_slug'] =sup_category.name
        category_list = Category.objects.filter(super_category=sup_category)
        context_dict['categories'] = category_list
        category_target = Category.objects.get(id=category_name_slug)
        context_dict['category_target'] = category_target

        #context_dict['page_name'] = page.title
        #pages = Page.objects.filter(id=page_name_slug)
        #context_dict['pages'] = pages
        page = Page.objects.get(id=page_name_slug)
        context_dict['page'] = page

        pages = Page.objects.filter(tags=page.tags)[:10]
        pages2 = Page.objects.filter(category=category_target,id = page.id)
        context_dict['pages'] = pages


        data = page.data
        data = data.replace("[link]","<a href=\"")
        data = data.replace("[/link]","\">")
        data = data.replace("[/nlink]","</a>")
        data = data.replace("[img]","<img src=\"")
        data = data.replace("[/img]","\">")

        data = data.replace("[center]","<center>")
        data = data.replace("[/center]","</center>")
        data = data.replace("[right]","<p align=\"right\">")
        data = data.replace("[/right]","</p>")
        data = data.replace("[left]","<p align=\"left\">")
        data = data.replace("[/left]","</p>")

        data = data.replace("[header]","<h3>")
        data = data.replace("[/header]","</h3>")
        data = data.replace("[bold]","<b>")
        data = data.replace("[/bold]","</b>")
        data = data.replace("[italic]","<i>")
        data = data.replace("[/italic]","</i>")

        data = data.replace("[subscript]","<sub>")
        data = data.replace("[/subscript]","</sub>")
        data = data.replace("[superscript]","<sup>")
        data = data.replace("[/superscript]","</sup>")
        data = data.replace("[highlight]","<mark>")
        data = data.replace("[/highlight]","</mark>")
        data = data.replace("[line]","<ins>")
        data = data.replace("[/line]","</ins>")
        data = data.replace("[block]","<blockquote>")
        data = data.replace("[/block]","</blockquote>")


        #video = data.partition('[video]')[0].rpartition('[/video]')[0]
        data = data.replace("[video]http://cis.eng.src.ku.ac.th","<iframe width=\"500\" height=\"350\" src=\"http://cis.eng.src.ku.ac.th")
        data = data.replace("[video]/media/documents/","<iframe width=\"500\" height=\"350\" src=\"/media/documents/")
        data = data.replace("[video]https://youtu.be/","<iframe width=\"500\" height=\"350\" src=\"https://www.youtube.com/embed/")
        data = data.replace("[video]http://youtu.be/","<iframe width=\"500\" height=\"350\" src=\"https://www.youtube.com/embed/")
        data = data.replace("[video]http://www.youtube.com/watch?v=","<iframe width=\"500\" height=\"350\" src=\"http://www.youtube.com/embed/")
        data = data.replace("[video]https://www.youtube.com/watch?v=","<iframe width=\"500\" height=\"350\" src=\"http://www.youtube.com/embed/")
        data = data.replace("[/video]","?wmode=opaque\" frameborder=\"0\" allowfullscreen></iframe>")

        context_dict['data'] = data
        context_dict['category'] = category
        comment = Comment.objects.filter(page=page).order_by('date')
        for run in comment:

            run.data = run.data.replace("[block]","<div class=\"well\">")
            run.data = run.data.replace("[/block]","</div>")
            run.data = run.data.replace("[link]","<a href=\"")
            run.data = run.data.replace("[/link]","\">")
            run.data = run.data.replace("[/nlink]","</a>")
            run.data = run.data.replace("[img]","<img src=\"")
            run.data = run.data.replace("[/img]","\" >")

            run.data = run.data.replace("[video]http://cis.eng.src.ku.ac.th","<iframe width=\"500\" height=\"350\" src=\"http://cis.eng.src.ku.ac.th")
            run.data = run.data.replace("[video]/media/documents/","<iframe width=\"500\" height=\"350\" src=\"/media/documents/")
            run.data = run.data.replace("[video]https://www.youtube.com/embed/","<iframe width=\"500\" height=\"350\" src=\"https://www.youtube.com/embed/")
            run.data = run.data.replace("[video]https://youtu.be/","<iframe width=\"500\" height=\"350\" src=\"https://www.youtube.com/embed/")
            run.data = run.data.replace("[video]http://youtu.be/","<iframe width=\"500\" height=\"350\" src=\"https://www.youtube.com/embed/")
            run.data = run.data.replace("[video]http://www.youtube.com/watch?v=","<iframe width=\"500\" height=\"350\" src=\"http://www.youtube.com/embed/")
            run.data = run.data.replace("[video]https://www.youtube.com/watch?v=","<iframe width=\"500\" height=\"350\" src=\"http://www.youtube.com/embed/")
            run.data = run.data.replace("[/video]","?wmode=opaque\" frameborder=\"0\" allowfullscreen></iframe>")

        context_dict['comments'] = comment
        likecomment = LikeComment.objects.all()

        cuser =request.user
        array = []
        for runc in comment:
            x = 0
            for runlike in likecomment:
                if runlike.comment == runc and runlike.user == cuser and x == 0:
                    x = 1
                    array.append(runc)
        context_dict['check_array'] = array
        context_dict['likecomments'] = likecomment
        clikepage = LikePage.objects.filter(page=page).count()
        context_dict['likepage'] = clikepage
        context_dict['user'] = request.user
        tags = TaggedItem.objects.filter(object_id=page.id)
        context_dict['tags'] = tags
    except Category.DoesNotExist:
        pass
    return render(request, 'knowledge_management/page.html', context_dict)

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return search(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'knowledge_management/add_category.html', {'form': form})

def newpost(request, do_command, to_page):
    if do_command != 'edit':

        if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                pages = form.save(commit=False)
                pages.views = 0
                pages.postby = request.user
                page_category = Category.objects.get(name=pages.category.name)
                page_supercategory = Super_category.objects.get(name=page_category.super_category)

                pages.save()
                page_id = pages.id

                url = reverse('knowledge_management.views.page', kwargs={'category_name_slug': page_category.id, 'page_name_slug': page_id,'supcategory_name_slug': page_supercategory.id })
                return HttpResponseRedirect(url)
            else:
                print(form.errors)
        else:
            form = PageForm()

        context_dict = {'form':form,}
        category_list = Category.objects.order_by('super_category')
        context_dict['categories'] = category_list
        if to_page != '0':
            edit_page = Page.objects.get(id=to_page)
            context_dict['edit_page'] = edit_page
        context_dict['categories'] = category_list
        context_dict['do_command'] = do_command

        tags = Tag.objects.order_by('name')
        array = []
        for run in range(len(tags)):
            x = str(tags[run])
            array.append(x)

        context_dict['tags'] = array

        return render(request, 'knowledge_management/newpost.html', context_dict)

    if do_command == 'edit':
        if request.method == 'POST':

            pages = Page.objects.get(id=to_page)
            pages.title = request.POST.get('title')
            pages.data = request.POST.get('data')
            pages.date = datetime.now()
            page_edit = Page.objects.get(id=to_page)
            page_category = Category.objects.get(name=pages.category.name)
            page_supercategory = Super_category.objects.get(name=page_category.super_category.name)
            pages.save()

            url = reverse('knowledge_management.views.page', kwargs={'category_name_slug': page_category.id, 'page_name_slug': page_edit.id,'supcategory_name_slug': page_supercategory.id })
            return HttpResponseRedirect(url)

        else:
            form = PageForm()


    if do_command == 'delete':
        pages = Page.objects.get(id=to_page)
        pages.delete()
        return category(request)


    context_dict = {'form':form,}
    edit_page = Page.objects.get(id=to_page)
    context_dict['edit_page'] = edit_page
    context_dict['edit_data'] = edit_page.data
    context_dict['do_command'] = do_command
    category_list = Category.objects.order_by('name')
    context_dict['categories'] = category_list
    tags = Tag.objects.order_by('name')
    array = []
    for run in range(len(tags)):
        x = str(tags[run])
        array.append(x)

    context_dict['tags'] = array

    return render(request, 'knowledge_management/newpost.html', context_dict)


def result(request):
    context_dict = {}
    s = request.GET['search']
    search = Page.objects.filter(Q(title__icontains=s)).order_by('-date')[:100]
    context_dict['name'] = s
    context_dict['result'] = search
    categorys = Category.objects.all()
    context_dict['categorys'] = categorys
    supcategorys = Super_category.objects.all()
    context_dict['supcategorys'] = supcategorys

    return render(request, 'knowledge_management/result.html', context_dict)

def tagresult(request, tag_name):
    context_dict = {}
    find = tag_name
    tagged = Page.objects.filter(Q(tags__icontains=find)).order_by('-date')[:100]
    context_dict['result'] = tagged
    context_dict['tag_name'] = tag_name
    categorys = Category.objects.all()
    context_dict['categorys'] = categorys
    supcategorys = Super_category.objects.all()
    context_dict['supcategorys'] = supcategorys

    return render(request, 'knowledge_management/tagresult.html', context_dict)

def likecomment(request, category_name_slug, page_name_slug, supcategory_name_slug, commentid):
    LikeComment.objects.create(
        comment=Comment.objects.get(id=commentid),
        user=request.user
    )
    comment = Comment.objects.get(id=commentid)
    comment.like = LikeComment.objects.filter(comment=comment).count()
    comment.save()

    url = reverse('knowledge_management.views.page', kwargs={'category_name_slug': category_name_slug, 'page_name_slug': page_name_slug,'supcategory_name_slug': supcategory_name_slug })
    return HttpResponseRedirect(url)


def likepage(request, supcategory_name_slug, category_name_slug, page_name_slug):
    LikePage.objects.create(
        page=Page.objects.get(id=page_name_slug),
        user=request.user
    )
    page = Page.objects.get(id=page_name_slug)
    page.like = page.like + 1
    page.save()

    url = reverse('knowledge_management.views.page', kwargs={'category_name_slug': category_name_slug, 'page_name_slug': page_name_slug,'supcategory_name_slug': supcategory_name_slug })
    return HttpResponseRedirect(url)


def index(request, check_status):
    x = check_status
    return render(request, 'knowledge_management/preview.html')


def list(request, check_status):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            limit = newdoc.docfile.url[-4:]
            file_type = ['.jpg','.png']
            newdoc.postby = request.user
            if limit in file_type:
                newdoc.save()
                url = reverse('knowledge_management.views.list', kwargs={'check_status': 1})
            else:
                url = reverse('knowledge_management.views.list', kwargs={'check_status': 0})
            # Redirect to the document list after POST
            #else:
                #return return render(request, 'knowledge_management/add_category.html')
            return HttpResponseRedirect(url)
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.order_by('-id')[:1]

    # Render list page with the documents and the form
    return render_to_response(
        'knowledge_management/preview.html',
        {'documents': documents, 'form': form, 'check_status': check_status},
        context_instance=RequestContext(request)
    )

def deletecomment(request, category_name_slug, page_name_slug, supcategory_name_slug, commentid):
    comment = Comment.objects.get(id=commentid)
    comment.delete()

    url = reverse('knowledge_management.views.page', kwargs={'category_name_slug': category_name_slug, 'page_name_slug': page_name_slug,'supcategory_name_slug': supcategory_name_slug })
    return HttpResponseRedirect(url)


def mypost(request, page):
    context_dict = {}

    sup_category = Super_category.objects.all()
    context_dict['sup_category'] = sup_category
    category = Category.objects.all()
    context_dict['category'] = category
    user = request.user


    x = (int(page)*20) - 20
    divide = Page.objects.filter(postby=user)
    if int(divide.count()%20) > 0 :
        carry = 1
    else:
        carry = 0
    numpage = range(1, (int(divide.count()/20)+carry)+1)
    context_dict['numpage'] = numpage
    pages = Page.objects.filter(postby=user).order_by('-date')[x:x+20]
    c = Page.objects.filter(postby=user)
    context_dict['c'] = c

    context_dict['pages'] = pages

    mypages = Page.objects.filter(postby=user).order_by('-date')[x:x+20]
    context_dict['mypages'] = mypages

    array = {}
    for runall in mypages:
        count_page = Comment.objects.filter(page = runall).count()
        array[runall] = count_page

    context_dict['array'] = array


    return render(request, 'knowledge_management/mypost.html', context_dict)

