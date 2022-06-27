var  button = document.querySelector('.send');
var data = document.querySelector('.inp');
var main=document.querySelector('.QA');
button.addEventListener("click", async function (event) {
    var inp = data.value;
    let reply;
    if (inp != "") {
        console.log(inp);
        reply = await rep(inp);
        question(inp);
        answer(await reply);
        data.value = "";
    }});
async function rep(r) {
    return await eel.resp(r)();
}
function question(d) {
    //create elements
    questiondiv=document.createElement("div");
    quest=document.createElement("p");
    div2=document.createElement("div");
    msg=document.createElement("div");
    img_div=document.createElement("div");
    img=document.createElement("img");
    //add classes
    questiondiv.classList.add('d-flex',"justify-content-start",'mb-4');
    msg.classList.add('msg_cotainer');
    img_div.classList.add('img_cont_msg');
    img.classList.add('rounded-circle','user_img_msg');
    img.style.width="40px";
    img.style.height="40px";
    img.style.marginTop ="20%";
    //define values
    quest.innerHTML=d;
    img.src='/data/pic.jpg';

    //apend child
    questiondiv.appendChild(img_div);
    img_div.appendChild(img);
    questiondiv.appendChild(msg);
    msg.appendChild(quest);
    main.append(questiondiv);
}
function answer(a){
        //create elements
        answerdiv=document.createElement("div");
        img_div=document.createElement("div");
        ans=document.createElement("p");
        img=document.createElement("img");
        msg=document.createElement("div");
        //add classes
        answerdiv.classList.add('d-flex','mb-4','justify-content-end');
        msg.classList.add('msg_cotainer_send');
        img_div.classList.add('img_cont_msg');
        img.classList.add('rounded-circle','user_img');
        img.style.width="40px";
        img.style.height="40px";
        img.style.marginTop ="20%";
        //define values
        ans.innerHTML= a;
        img.src='/data/bot.png';
        //append child
        answerdiv.appendChild(msg);
        answerdiv.appendChild(img_div);
        img_div.appendChild(img);
        msg.appendChild(ans);
        main.append(answerdiv);
}