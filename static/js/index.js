//? Execute after document ready
$(
    function () {
        getChart('left-upper-chart', 'leftUpperChart');
        getChart('left-bottom-chart', 'leftBottomChart');
        getChart('mid-bottom-chart', 'midBottomChart');
        getChart('right-upper-chart', 'rightUpperChart');
        getChart('right-bottom-chart', 'rightBottomChart')
    }
)


function getChart(eleID, eleUrl) {
    var chartLeftUpper = echarts.init(
        document.getElementById(eleID), 'darktheme', 
        { renderer: 'canvas' }
    );
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/" + eleUrl,
        dataType: 'json',
        success: function (result) {
            chartLeftUpper.setOption(result);
        }
    });
}