function getdata() {
    var user=document.getElementById("code").value;
    //firebase data retrieval function
    //path of your data
    //.once will get all your data in one time
    firebase.database().ref('code/'+code).once('value').then(function (snapshot) {
        //here we will get data
        //enter your field name
        var name=snapshot.val().codeName;
        var email=snapshot.val().codeEmail;
        var cnumber=snapshot.val().codeCnumber;
        var alternate=snapshot.val().codeAlternate;
        var address=snapshot.val().codeAddress;

        //now we have data in variables
        //now show them in our html

        document.getElementById("name").innerHTML=name;
        document.getElementById("email").innerHTML=email;
        document.getElementById("cnumber").innerHTML=cnumber;
        document.getElementById("alternate").innerHTML=alternate;
        document.getElementById("address").innerHTML=address;
    })
}