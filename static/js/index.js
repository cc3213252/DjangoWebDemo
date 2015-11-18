$(function(){
   $('#sms_query').click(smsQuery);

   $('#sms_add').click(function(){
     $('#myModal').modal("toggle");
     $('#myModal').on("shown.bs.modal", function(){
        $('#sm_name').val("");
        $('#sm_sex').val("");
        $('#sm_type').val("");
        $('#myModalLabel').text('Add One Item');
      });
   });

   $('#add_ok').click(function(){
      $('#sm_name').parent().removeClass("has-error");
      if ($('#sm_name').val() == ""){
        $('#sm_name').parent().addClass("has-error");
      }

      $('#sm_sex').parent().removeClass("has-error");
      if ($('#sm_sex').val() == ""){
        $('#sm_sex').parent().addClass("has-error");
      }

      $('#sm_type').parent().removeClass("has-error");
      if ($('#sm_type').val() == ""){
        $('#sm_type').parent().addClass("has-error");
      }

      var id = $('#myModalLabel').attr("name");
      var name = $('#sm_name').val();
      var sex = $('#sm_sex').val();
      var type = $('#sm_type').val();
      var title = $('#myModalLabel').text();

      if (title == "Add One Item"){
          $.post("/add_user_info_list", {"NAME": name, "SEX": sex, "TYPE":type}, function(result){
              $('#table').append(createTableLine(result));
          });
      }else{
          var user_info_list = id + "," + name + "," + sex + "," + type;

          $.post("/update_user_info_list", {"USER_INFO_LIST": user_info_list}, function(result){
             $('#myModal').hide();
             var line = findTableLine(id);
              if (line != null) {
                line.children[1].innerHTML = name;
                line.children[2].innerHTML = sex;
                line.children[3].innerHTML = type;
              }
          });
      }
    });
    $('#sm_forms').submit(function(e){
      e.preventDefault();
    })
})

function findTableLine(id){
  var list = $('#table').children();
  for (var index = 0; index < list.length; index++ ) {
    var  line = list[index];

    if (line.children[0].innerHTML == id) {
      return line;
    }
  }
}

function createTable(result){
  $.each(result, function(index, row){
    $('#table').append(createTableLine(row));
  });
}

function createTableLine(row){
       var trNode = document.createElement("tr");
     var tdnodeId = document.createElement("td");
     tdnodeId.innerHTML = row.id;
     tdnodeId.setAttribute("class", "id");

     var tdnodeName = document.createElement("td");
    tdnodeName.innerHTML = row.name;
    tdnodeName.setAttribute("class", "name");

    var tdnodeSex = document.createElement("td");
    tdnodeSex.innerHTML = row.sex;
    tdnodeSex.setAttribute("class", "sex");

    var tdnodeType = document.createElement("td");
    tdnodeType.innerHTML = row.type;
    tdnodeType.setAttribute("class", "type");

    var tdnodeBtn = document.createElement("td");
    var aNode1 = document.createElement("a");
    aNode1.setAttribute("class", "navbar-btn");
    var spanNode = document.createElement("span");
    spanNode.setAttribute("class", "glyphicon glyphicon-pencil");
    aNode1.appendChild(spanNode);
    aNode1.onclick = editStaff;
    aNode1.appendChild(spanNode);
    tdnodeBtn.appendChild(aNode1);


    var tdnodeBtn2 = document.createElement("td");
    var spanNode2 = document.createElement("span");
    var aNode2 = document.createElement("a");
    aNode2.setAttribute("class", "navbar-btn");
    spanNode2.setAttribute("class", "glyphicon glyphicon-trash");
    aNode2.onclick = deleteFun;
    aNode2.appendChild(spanNode2);
    tdnodeBtn2.appendChild(aNode2);

    trNode.appendChild(tdnodeId);
    trNode.appendChild(tdnodeName);
    trNode.appendChild(tdnodeSex);
    trNode.appendChild(tdnodeType);
    trNode.appendChild(tdnodeBtn);
    trNode.appendChild(tdnodeBtn2);
  return trNode;
}

function editStaff(){
  $('#myModal').modal('toggle')
  var id = $(this).parent().parent().children(".id").text();
  var name = $(this).parent().parent().children(".name").text();
  var sex = $(this).parent().parent().children(".sex").text();
  var type = $(this).parent().parent().children(".type").text();
  $('#myModal').on("shown.bs.modal", function(){
  $('#myModalLabel').attr("name", id);
  $('#sm_name').val(name);
  $('#sm_sex').val(sex);
  $('#sm_type').val(type);
  $('#myModalLabel').text('Update One Item');
  });
}

function deleteFun() {
  var id = $(this).parent().parent().children(".id").text();
  var node = $(this).parent().parent();

  $.post("/delete_user_info_list", {"ID": id}, function (result) {
     node.remove();
  });
}

function smsQuery(){
  var name = $('#sms_name').val();
  var sex = $('#sms_sex').val();
  var type = $('#sms_type').val();

  $.post("/get_user_info_list", {"NAME": name, "SEX":sex, "TYPE":type}, function(result){
    $.each($('#table').children(), function(index, line){
      line.remove();

    });
    createTable(result);
  });
}