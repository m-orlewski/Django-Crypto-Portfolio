// Function that manages a pop-up window for a Crypto buying form.
function show_window()
{
    var list = document.getElementById('window-app');
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
        });
    }
}

// Function that manages a pop-up window for a Crypto balance graph.
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
            list.style.display = "none";
            showBalance(this.id);
            
        });
    }
}

// Function that manages a pop-up window for a Crypto price prediction.
function show_window3()
{
    var list = document.getElementById('window-app3');
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
            select_coin(this.id);
        });
    }
}

// Function that gets a list of Cryptocurrencies to choose from.
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

// Function that redirects to Crypto buing form.
function sendId(id)
{
    var params = [];
    params.push("id=" + id);
    console.log(id);
    location.href = "http://localhost:8000/portfolio/profile/form?" + params.join("&");
}

// Function that selects a Crypto on homepage to show it's predicted value.
function select_coin(id)
{
    var params = [];
    params.push("id=" + id);
    console.log(id);
    location.href = "http://localhost:8000/portfolio?" + params.join("&");
}

// Function that selects a Crypto on profile to show current price of it.
function showBalance(id)
{
    var params = [];
    params.push("balance=" + id);
    console.log(id);
    location.href = "http://localhost:8000/portfolio/profile?" + params.join("&");
}
