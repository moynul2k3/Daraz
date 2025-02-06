from django import forms 
from .models import ColorFamily, Product, Brand, MainMaterial, WarrantyPeriod, ListedYearSeason, MensTrend
from mainapp.models import SubCategory, Group

FORM_CLASSES = 'w-full pe-5 text-sm bg-transparent appearance-none border-0 focus:ring-0'
class NewColorFamily(forms.ModelForm):
    class Meta:
        model = ColorFamily
        fields = ['name', 'color']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Your ColorFamily name'}),
            'color': forms.TextInput(attrs={'class': FORM_CLASSES, 'placeholder': 'Enter Your color'})
        }







FORM_INPUT_CLASSES = 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-[#01acff] peer'

# ...............................................................NEW CREATION FORM................................................................
class NewProduct(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].empty_label = 'Select Product Category'
        self.fields['subcategory'].empty_label = 'Select Product Sub-Category'
        self.fields['group'].empty_label = 'Select Product Group'
        self.fields['subcategory'].queryset = SubCategory.objects.none()
        self.fields['group'].queryset = Group.objects.none()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set
            
        if 'subcategory' in self.data:
            try:
                subcategory_id = int(self.data.get('subcategory'))
                self.fields['group'].queryset = Group.objects.filter(subcategory_id=subcategory_id)
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['group'].queryset = self.instance.subcategory.group_set
            
    
    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'group', 'name', 'description', 'price', 'discount', 'color_family', 'image', 'brand', 'sku', 'flash_sale', 'is_sold' ]
        
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-md border-[#01acff]'
                }),
            'subcategory': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-md border-[#01acff]'
                }),
            'group': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-md border-[#01acff]'
                }),
            'name': forms.TextInput(attrs={
                'name': 'name',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write Your Product Descriptions',
                'class': 'w-full h-auto p-3 bg-transparent border-[1px] border-black/10 rounded-lg',
                'rows': '14'
                }),
            'price': forms.TextInput(attrs={
                'name': 'price',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'discount': forms.TextInput(attrs={
                'name': 'discount',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'color_family': forms.Select(attrs={'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-s-md border-[#01acff]'}),
            'image': forms.FileInput(attrs={'class': FORM_CLASSES}),
            'brand': forms.TextInput(attrs={
                'name': 'brand',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'sku': forms.TextInput(attrs={
                'name': 'sku',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'flash_sale': forms.CheckboxInput(attrs={'class': 'w-[20px] h-[20px] pe-5 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'is_sold': forms.CheckboxInput(attrs={'class': 'w-full pe-5 text-sm bg-transparent'}),
        }
        
# ...............................................................EDIT FORM................................................................
class EditProduct(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].empty_label = 'Select Product Category'
        self.fields['subcategory'].empty_label = 'Select Product Sub-Category'
        self.fields['group'].empty_label = 'Select Product Group'
        self.fields['subcategory'].queryset = SubCategory.objects.none()
        self.fields['group'].queryset = Group.objects.none()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set
            
        if 'subcategory' in self.data:
            try:
                subcategory_id = int(self.data.get('subcategory'))
                self.fields['group'].queryset = Group.objects.filter(subcategory_id=subcategory_id)
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['group'].queryset = self.instance.subcategory.group_set
            
    
    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'group', 'name', 'description', 'price', 'discount', 'image', 'sku']
        
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-md border-[#01acff]'
                }),
            'subcategory': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-md border-[#01acff]'
                }),
            'group': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-transparent border-[1px] rounded-md border-[#01acff]'
                }),
            'name': forms.TextInput(attrs={
                'name': 'name',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write Your Product Descriptions',
                'class': 'w-full h-auto p-3 bg-transparent border-[1px] border-black/10 rounded-lg',
                'rows': '14'
                }),
            'price': forms.TextInput(attrs={
                'name': 'price',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'discount': forms.TextInput(attrs={
                'name': 'discount',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
            'image': forms.FileInput(attrs={'class': FORM_CLASSES}),
            'sku': forms.TextInput(attrs={
                'name': 'sku',
                'placeholder': ' ',
                'class': FORM_INPUT_CLASSES
                }),
        }
        
        
# ..............................................................Manage Products Form ....................................................
class ManageProduct(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id', None)
        super(ManageProduct, self).__init__(*args, **kwargs)
        
        self.fields['location'].initial = 1 
        self.fields['warranty_type'].initial = 1 
        self.fields['location'].empty_label = 'International'
        self.fields['brand'].empty_label = 'Select Product Brand'
        self.fields['main_material'].empty_label = 'Select Product Main Material'
        self.fields['warranty_type'].empty_label = 'Select Product Warranty Type'
        self.fields['warranty_period'].empty_label = 'Select Product Warranty Period'
        self.fields['listed_year_season'].empty_label = 'Select Product Listed Year Season'
        self.fields['mens_trend'].empty_label = 'Select Product Mens Trend'
        
        self.fields['brand'].queryset = Brand.objects.none()
        self.fields['main_material'].queryset = MainMaterial.objects.none()
        self.fields['warranty_period'].queryset = WarrantyPeriod.objects.none()
        self.fields['listed_year_season'].queryset = ListedYearSeason.objects.none()
        self.fields['mens_trend'].queryset = MensTrend.objects.none()
        if group_id:
            self.fields['brand'].queryset = Brand.objects.filter(group_id=group_id)
            self.fields['main_material'].queryset = MainMaterial.objects.filter(group_id=group_id)
            self.fields['warranty_period'].queryset = WarrantyPeriod.objects.filter(group_id=group_id)
            self.fields['listed_year_season'].queryset = ListedYearSeason.objects.filter(group_id=group_id)
            self.fields['mens_trend'].queryset = MensTrend.objects.filter(group_id=group_id)
    class Meta:
        model = Product
        fields = ['location', 'brand', 'image', 'main_material', 'warranty_type', 'warranty_period', 'listed_year_season', 'mens_trend', 'flash_sale', 'wholesale_price', 'everyday_low_price', 'free_delivery', 'fashion', 'beauty_glamour', 'mart', 'home_makeover', 'best_price_guaranteed', 'is_sold']
        
        widgets = {
            'location': forms.Select(attrs={
                'class': 'w-full h-8 pe-5 py-0 text-sm rounded-lg border-[1px]  border-[#01acff] flex justify-center items-center'
                }),
            'brand': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-[#01acff20] border-[1px] rounded-sm border-[#01acff] '
                }),
            'main_material': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-[#01acff20] border-[1px] rounded-sm border-[#01acff] '
                }),
            'warranty_type': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-[#01acff20] border-[1px] rounded-sm border-[#01acff] '
                }),
            'warranty_period': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-[#01acff20] border-[1px] rounded-sm border-[#01acff] '
                }),
            'listed_year_season': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-[#01acff20] border-[1px] rounded-sm border-[#01acff] '
                }),
            'mens_trend': forms.Select(attrs={
                'class': 'w-full pe-5 text-sm bg-[#01acff20] border-[1px] rounded-sm border-[#01acff] '
                }),
            'image': forms.FileInput(attrs={'class': 'hidden', 'id': 'dropzone-file', 'type': "file"}),
            'flash_sale': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'wholesale_price': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'everyday_low_price': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'free_delivery': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'fashion': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'beauty_glamour': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'mart': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'home_makeover': forms.CheckboxInput(attrs={'class': ' p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'best_price_guaranteed': forms.CheckboxInput(attrs={'class': 'p-1 text-sm bg-transparent border-2 border-[#01acff] rounded-sm ring-0 focus:ring-0'}),
            'is_sold': forms.CheckboxInput(attrs={'class': ' p-1 text-sm border-2 rounded-sm ring-0 focus:ring-0', 'style': 'border: 2px solid red; accent-color: red;'}),
        }


