// Constants
var MAX_UPLOAD_FILE_SIZE = 1024*1024; // 1 MB
var UPLOAD_URL = "/upload";
var NEXT_URL   = "/files/";

// List of pending files to handle when the Upload button is finally clicked.
var PENDING_FILES  = [];


$(document).ready(function() {
    // Set up the handler for the file input box.
    $("#file-picker").on("change", function() {
        handleFiles(this.files);
    });

    // Handle the submit button.
    $("#upload-button").on("click", function(e) {
        // If the user has JS disabled, none of this code is running but the
        // file multi-upload input box should still work. In this case they'll
        // just POST to the upload endpoint directly. However, with JS we'll do
        // the POST using ajax and then redirect them ourself when done.
        e.preventDefault();
        doUpload();
    })
});


function doUpload() {
    $("#progress").show();
    var $progressBar   = $("#progress-bar");

    // Gray out the form.
    $("#upload-form :input").attr("disabled", "disabled");

    // Initialize the progress bar.
    $progressBar.css({"width": "0%"});

    // Collect the form data.
    fd = collectFormData();

    // Attach the files.
    for (var i = 0, ie = PENDING_FILES.length; i < ie; i++) {
        // Collect the other form data.
        fd.append("file", PENDING_FILES[i]);
    }

    console.log("Attached fd : "+fd);
    // Inform the back-end that we're doing this over ajax.
    fd.append("__ajax", "true");

    var xhr = $.ajax({
        xhr: function() {
            var xhrobj = $.ajaxSettings.xhr();
            if (xhrobj.upload) {
                xhrobj.upload.addEventListener("progress", function(event) {
                    var percent = 0;
                    var position = event.loaded || event.position;
                    var total    = event.total;
                    if (event.lengthComputable) {
                        percent = Math.ceil(position / total * 100);
                    }

                    // Set the progress bar.
                    $progressBar.css({"width": percent + "%"});
                    //$fileProgress.text("File Progress : "+percent + "%");
                    document.getElementById('fileProgress').innerHTML = "❖  File Progress : "+percent + "%   ❖";
                    if (percent == 100){
                      document.getElementById("done-btn").disabled = false;
                    }
                }, false)
            }
            return xhrobj;
        },
        url: UPLOAD_URL,
        method: "POST",
        contentType: false,
        processData: false,
        cache: false,
        data:fd,
        success: function(data) {
            $progressBar.css({"width": "100%"});
            console.log("Yuck Yes...!"+data);
        },
    });
}


function collectFormData() {
    // Go through all the form fields and collect their names/values.
    var fd = new FormData();

    $("#upload-form :input").each(function() {
        var $this = $(this);
        var type  = $this.attr("type") || "";
        var value = $this.val();

        fd.append(name, value);
    });

    console.log("This is FD "+fd)
    return fd;
}


function handleFiles(files) {
    // Add them to the pending files list.
    for (var i = 0, ie = files.length; i < ie; i++) {
        PENDING_FILES.push(files[i]);
    }
}

function upload(){
  document.getElementById("body-elements").innerHTML='<fieldset id="progress" style="display: none"> <legend id=fileProgress>Files Progress</legend>   <div class="progress-trough"> <div id="progress-bar" class="progress-bar"></div></div> <button id= "done-btn" type = submit onclick="uploadDone()">Done </button> <div id="Thanks-note" >Thanks for using DASH.</div></fieldset>';
  document.getElementById("done-btn").disabled = true;
}

function uploadDone(){
  console.log("This is clicked!")
window.location.reload();
}
