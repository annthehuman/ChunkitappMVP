$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on('submit',"#post-form-1",function(e) {
    e.preventDefault();
    var searchIDs = $('.checkbox1:checked').map(function(){
      return $(this).val();
    }).get();
    $.ajax({
        type: 'POST',
        url: '/data/',
        data: {
            question:question,
            check: searchIDs,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            index: id,
},
    })
});
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on('submit',"#post-form-2",function(e) {
    e.preventDefault();
    var searchIDs = $('.checkbox2:checked').map(function(){
      return $(this).val();
    }).get();
    $.ajax({
        type: 'POST',
        url: '/data/',
        data: {
            question:question,
            check: searchIDs,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            index: id,
},
    })
});
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on('submit',"#post-form-3",function(e) {
    e.preventDefault();
    var searchIDs = $('.checkbox3:checked').map(function(){
      return $(this).val();
    }).get();
    $.ajax({
        type: 'POST',
        url: '/data/',
        data: {
            question:question,
            check: searchIDs,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            index: id,
},
    })
});
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on('submit',"#post-form-4",function(e) {
    e.preventDefault();
    var searchIDs = $('.checkbox4:checked').map(function(){
      return $(this).val();
    }).get();
    $.ajax({
        type: 'POST',
        url: '/data/',
        data: {
            question:question,
            check: searchIDs,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            index: id,
},
    })
});
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on('submit',"#post-form-5",function(e) {
    e.preventDefault();
    var searchIDs = $('.checkbox5:checked').map(function(){
      return $(this).val();
    }).get();
    $.ajax({
        type: 'POST',
        url: '/data/',
        data: {
            question:question,
            check: searchIDs,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            index: id,
},
    })
});
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-6",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox6:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-7",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox7:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-8",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox8:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-9",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox9:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-10",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox10:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-11",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox11:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-12",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox12:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-13",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox13:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-14",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox14:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-15",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox15:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-16",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox16:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-17",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox17:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-18",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox18:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-19",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox19:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-20",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox20:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-21",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox21:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-22",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox22:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-23",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox23:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-24",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox24:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-25",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox25:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-26",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox26:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-27",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox27:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-28",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox28:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-29",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox29:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-30",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox30:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-31",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox31:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-32",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox32:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-33",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox33:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-34",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox34:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-35",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox35:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-36",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox36:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-37",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox37:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-38",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox38:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-39",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox39:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-40",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox40:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-41",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox41:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-42",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox42:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
    
});

$(function (){ 
   var question = null;
    $(':input').focus(function() {
      question = $(this).val();
    });


 $(document).on("submit","#post-form-43",function(e) {
    e.preventDefault(); 
    var searchIDs = $(".checkbox43:checked").map(function(){ 
      return $(this).val();
    }).get(); 
    $.ajax({ 
        type: "POST", 
        url: "/data/", 
        data: {
            question:question,
            check: searchIDs, 
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), 
            index: id, 
    }, 
    }) 
    });
});

var first_order = [1, 2, 3];
var order = first_order.concat(django_order);

function* iterateArray(array) {
  for (const entry of array) {
    yield entry;
  }
}
const iterator = iterateArray(order);

const adapter = iterator => () => {
  const entry = iterator.next();

  return entry.value;
};

const next = adapter(iterator);


var id
var id_next
var myAudio



    function nextpart() {
        window.id = next();
        var index = order.indexOf(id);
        window.id_next = order[index + 1];
        window.myAudio = document.getElementById('Player_'+id);
    };


    function audioplay() {
        myAudio.play();
        isPlaying = true;
        document.getElementById('instructions_1').style.display = 'none';
        document.getElementById('practice_'+id).style.display = 'block';
    };

    function togglePlay() {
      if (isPlaying) {
        myAudio.pause();
        isPlaying = false;
        document.getElementById('text_'+id).style.display='none';
      }  else {
        myAudio.play();
        isPlaying = true;
        document.getElementById('text_'+id).style.display='block';
      }

    };

    function audioend() {
        document.getElementById("popup_"+id).style.display = "block";
        document.getElementById("practice_"+id).style.display = "none";
};




num = 1
function nextstep() {
    if (id_next === undefined) {
        num = 43;
    } else {
    num++;
    var step = document.getElementById('step');
    step.innerHTML = "Vaihe "+num+"/43";
}
};

    function handler(lnk_obj){
      lnk_obj.innerHTML = (lnk_obj.innerHTML == 'Tauko') ? 'Edetä' : 'Tauko' ;
    };