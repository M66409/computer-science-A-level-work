function dark_mode(){

    var html=document.querySelector("html")
    html.classList.toggle("html_dark")

    var nav_bar = document.getElementById("nav-bars")
    nav_bar.classList.toggle("nav-bar_dark")

    var h1 = document.getElementById("h1")
    h1.classList.toggle("h1_dark")

    var nav_active = document.getElementById("active")
    nav_active.classList.toggle("active_dark")
    
    var lists = document.querySelectorAll(".lists")
    for(let i=0;i<lists.length;i++){
        lists[i].classList.toggle("lists_dark")
    }

    var pgraph = document.querySelectorAll("p")
    for(let i=0; i<pgraph.length ;i++){
        pgraph[i].classList.toggle("p_dark")
    }

    var nav_paragraph = document.getElementById("nav-bar-paragraph")
    nav_paragraph.classList.toggle("nav-bar_paragraphs")
    
    var tr_even=document.querySelectorAll("table tr:nth-child(even)")
    for(let i =0; i<tr_even.length; i++){
        tr_even[i].classList.toggle("tr_even_dark")
    }

    var tr_odd=document.querySelectorAll("table tr:nth-child(odd)")
    for( let i = 0; i<tr_odd.length; i++){
        tr_odd[i].classList.toggle("tr_odd_dark")
    }

    var input=document.querySelectorAll("input")
    for(let i=0; i<input.length; i++){
        input[i].classList.toggle("input_dark")
    }

    var text=document.querySelector("textarea")
    text.classList.toggle("textarea_dark")
}