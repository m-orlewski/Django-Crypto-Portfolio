function show_window(type)
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
            if (type) {
                select_coin(this.id);
            } else {
                sendId(this.id);
            }
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

function show_window2()
{
    var list = document.getElementById('window-app2');
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
            console.log('eee')
            list.style.display = "none";
            showBalance(this.id);
            
        });
    }
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
    console.log(id);
    location.href = "http://localhost:8000/portfolio/profile/form?" + params.join("&");
}


function select_coin(id)
{
    var params = [];
    params.push("id=" + id);
    console.log(id);
    location.href = "http://localhost:8000/portfolio?" + params.join("&");
}

function showBalance(id)
{
    var params = [];
    params.push("balance=" + id);
    console.log(id);
    location.href = "http://localhost:8000/portfolio/profile?" + params.join("&");
}

function show(){
    var list = document.getElementById("user_port");
    var butt = document.getElementById("show_button");
    if(list.style.display == "block"){
        list.style.display = "none";
        butt.innerText = "Show Portfolio";
    }
    else{
        list.style.display = "block";
        butt.innerText = "Hide Portfolio";
    }
}
