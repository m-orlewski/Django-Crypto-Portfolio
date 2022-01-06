function show_window()
{
    var list = document.getElementById('window-app');
    var buymenu = document.getElementById('window-app-buy');
    list.style.display="block";

    window.addEventListener("click", function(event)
    {
        if(event.target == list)
        {
            list.style.display = "none";
        } 
    });

    var coll = document.getElementsByClassName("collapsible");
    for (var i = 0; i < coll.length; i++)
    {
        coll[i].addEventListener("click", function()
        {
            list.style.display = "none";
            sendId(this.id);
            //buymenu.style.display = "block";
        });
    }
    /*
    window.addEventListener("click", function(event)
    {
        if(event.target == buymenu)
        {
            list.style.display = "block";
            buymenu.style.display = "none";
        }
    });
    */
}

function search()
{
    var input, elements, txtValue, filter;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    elements = document.getElementsByClassName("collapsible");
    for(var i = 0; i<elements.length; i++){
        var a = elements[i];
        txtValue = a.textContent || a.innerText;
        if(txtValue.toUpperCase().indexOf(filter) > -1){
            elements[i].style.display = "";
        }
        else{
            elements[i].style.display = "none";
        }
    }
}


function calculate()
{
    var val = document.getElementById('inputAmount');
    document.getElementById('amount').innerHTML = val.value;
}

function sendId(id)
{
    var params = [];
    params.push("id=" + id);
    location.href = "http://localhost:8000/portfolio/profile/form?" + params.join("&");
}