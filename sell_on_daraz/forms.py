from mainapp.models import Banner, Category, SubCategory, Group
from product.models import Brand, MainMaterial, WarrantyPeriod, ListedYearSeason, MensTrend
from django import forms


FORM_CLASSES = 'w-full pe-2 text-sm bg-transparent appearance-none border-0 focus:ring-0'
# ...............................................................NEW CREATION FORM................................................................
class NewBanner(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['name', 'image']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Banner Name'}),
            'image': forms.FileInput(attrs={'class': FORM_CLASSES}),
        }
        
class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Category Name'}),
        }
                
class NewSubCategory(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].empty_label = 'Select Product Category'
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        
        widgets = {
            'category': forms.Select(attrs={'class': FORM_CLASSES}),
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Sub-Category Name'}),
        }
        
        
class NewGroup(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].empty_label = 'Select Product Category'
        self.fields['subcategory'].empty_label = 'Select Product Sub-Category'
        self.fields['subcategory'].queryset = SubCategory.objects.none()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set
            
    class Meta:
        model = Group
        fields = ['category', 'subcategory', 'name', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': FORM_CLASSES}),
            'subcategory': forms.Select(attrs={'class': FORM_CLASSES}),
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Group Name'}),
            'image': forms.FileInput(attrs={'class': FORM_CLASSES}),
        }


class NewBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Brand Name'}), 
        }


class NewMaterial(forms.ModelForm):
    class Meta:
        model = MainMaterial
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Material Name'}), 
        }


class NewWarrantyPeriod(forms.ModelForm):
    class Meta:
        model = WarrantyPeriod
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Warranty Period'}), 
        }


class NewListedYearSeason(forms.ModelForm):
    class Meta:
        model = ListedYearSeason
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Listed Year Season'}), 
        }


class NewMensTrend(forms.ModelForm):
    class Meta:
        model = MensTrend
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Mens Trend'}), 
        }





# ................................................................EDIT FORM.................................................................
class EditBanner(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['name', 'image']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Banner Name'}),
            'image': forms.FileInput(attrs={'class': FORM_CLASSES}),
        }
        
class EditCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Category Name'}),
        }
        
class EditSubCategory(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        
        widgets = {
            'category': forms.Select(attrs={'class': FORM_CLASSES}),
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Category Name'}),
        }
        
class EditGroup(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].empty_label = 'Select Product Category'
        self.fields['subcategory'].empty_label = 'Select Product Sub-Category'
        self.fields['subcategory'].queryset = SubCategory.objects.none()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set
            
    class Meta:
        model = Group
        fields = ['category', 'subcategory', 'name', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': FORM_CLASSES}),
            'subcategory': forms.Select(attrs={'class': FORM_CLASSES}),
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Group Name'}),
            'image': forms.FileInput(attrs={'class': FORM_CLASSES}),
        }
        