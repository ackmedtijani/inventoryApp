var purchase_menu = document.getElementById('purchase-menu');
var product_menu = document.getElementById('product-menu');
var cashinventory_menu = document.getElementById('cashinventory-menu');
var table_product = document.getElementById('table-products')
var table_purchase = document.getElementById('table-purchases');
var search = document.getElementById('search');
var add_new = document.querySelector('.add-new');
var edit = document.querySelectorAll('.edit-btn');
var edit_modal = document.getElementById('edit-product-modal');



loadEventListeners();

function loadEventListeners(){
    product_menu.addEventListener('click' , function(){
        toggleLinksAndTable(product_menu , table_product);
    });

    purchase_menu.addEventListener('click' , function() {
        toggleLinksAndTable(purchase_menu , table_purchase);

    });

    search.addEventListener('click' , function(){
        var search_modal = document.getElementById('search-modal');
        displayModal(search_modal);
        window.onclick = function(event) {
            if (event.target == search) {
                console.log(event);
        search.style.display = "none";

            }
        }

    });

  
    add_new.addEventListener('click' , function(){
        var product_add_modal = document.getElementById('add-product-modal');
        displayModal(product_add_modal);
        window.onclick = function(event) {
            if (event.target == product_add_modal) {
                console.log(event);
        product_add_modal.style.display = "none";

            }
        }
    })

    edit.forEach(function (item) {

        item.addEventListener('click' , function(){

        const request = new XMLHttpRequest();


        
        var edit_id = item.id;

        if (item.classList.contains('product')){
            url = '/edit/product/' + edit_id;
        }

        else{
            url = '/edit/purchase/' + edit_id;
        }

        edit_modal_btn = edit_modal.children[1];
        edit_form = edit_modal.children[0];
        console.log(edit_modal_btn);

        request.open('GET' ,  url , true);
        request.onload = function(){
            if(this.status === 200){
                edit_form.innerHTML = this.responseText;
                edit_modal.style.display = 'block';
                edit_form.action = url;
            }
        }

        request.send();    

    });

    });

}


function check_current(element){
    return !element.classList.contains('current');
        
}

function check_table_current(element){
    return !element.classList.contains('table-current');
}

function toggleLinksAndTable(linkElement , tableElement){
    var current_link = document.querySelector('.current');
    var table_current = document.querySelector('.table-current');
    if (check_current(linkElement) ){
        current_link.classList.remove('current');
        linkElement.classList.add('current');
    }

    if (check_current(tableElement)){
        table_current.classList.remove('table-current');
        tableElement.classList.add('table-current');

    }


}

function displayModal(modal){
    if (modal.style.display == 'none'){
        modal.style.display = 'block';
    }        
    else{
        modal.style.display = 'none';
    }

}



    

