from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def contact_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        contacts = Contact.objects.filter(name__icontains=search_query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Contact Added Successfully!')
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Add Contact'
    })
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, 'Contact Updated Successfully!')
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Edit Contact'
    })



def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact Deleted Successfully!')
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
