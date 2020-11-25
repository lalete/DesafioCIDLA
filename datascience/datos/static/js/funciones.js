$(document).ready(Principal)

function Principal() {
    //$("#archijson").click(Grafico1);
    $("#boton2").click(Grafico2);
    $("#boton3").click(Grafico3);
    $("#boton4").click(Grafico4);
}

function Grafico1() {


    var graf = new CanvasJS.Chart('grafico', {
        axisY: {
            title: "Grafico"
        },
        axisX: {
            title: "Value"
        },
        data: [{
            color: "red",
            type: "line",
            dataPoints: []
        }]
    });
    for (i = 0; i < ({
            {}.length); i++) {
            graf.options.data[0].dataPoints.push({
                y: {
                    {
                        x
                    }
                } [i]
            });


        }

        graf.render();

    }

   