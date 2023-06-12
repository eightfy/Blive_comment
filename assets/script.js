$(document).ready(function() {
    var scrolling = false;
    var scrollTimeout = null;
    var bottomButton = $("#bottom-button");

    $("#comments").scroll(function() {
        if ($(this).scrollTop() + $(this).innerHeight() >= this.scrollHeight) {
            scrolling = true;
            bottomButton.hide();
        } else {
            scrolling = false;
            bottomButton.show();
        }
    });
    var lastLineNum = 0; // 记录上一次的行号
    setInterval(function() {
        $.ajax({
            url: "http://localhost:8000/data.txt",
            dataType: "text",
            beforeSend: function(xhr) {
        xhr.overrideMimeType("text/html;charset=gbk");
            },
            success: function(data) {
                var lines = data.split('\n');
                var newLines = lines.slice(lastLineNum); // 只保留从上一次行号之后的新行
                newLines.forEach(function(line, index) {
                    if (line.length > 0) {
                        var parts = line.split('：：');
                        if (parts.length >= 2) {
                            var message = parts[1].substr(0, parts[1].length - 1);
                            var html = `<div class="comment">
                                <span class="author">${parts[0]}</span>
                                <span class="content">${message}</span>
                                <span class="time">${(new Date()).toLocaleTimeString()}</span>
                            </div>`;
                            $("#comments").append(html);
                            //console.log(lastLineNum)
                            if (scrolling) {
                                $("#comments").scrollTop($("#comments")[0].scrollHeight);
                            } else {
                                bottomButton.show();
                            }
                            if ($("#comments").prop("scrollHeight") - $("#comments").scrollTop()- $("#comments").innerHeight() <= 200) {
                                $("#comments").scrollTop($("#comments")[0].scrollHeight);
                            }
                        }
                    }
                });
                lastLineNum = lines.length - 1; // 更新上一次行号
                //console.log(lastLineNum);
            }
        });
        //console.log(newLines);
    }, 100);

    bottomButton.click(function() {
        $("#comments").scrollTop($("#comments")[0].scrollHeight);
        bottomButton.hide();
        scrolling = true;
        scrollTimeout = setTimeout(function() {
            scrolling = false;
        }, 1000);
    });
});