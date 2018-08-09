



function render_index(query_sample_id) {

    d3.json("/metadata/" + query_sample_id, function (error, response) {
        let sample_id = parseInt(query_sample_id.split("_")[1]).pad(4);
        console.log("Response from /metadata/" + query_sample_id, "response= ", response);
        if (error) return console.warn(error);

        render_metadata_table(
            "metadata-table",
            response[0],
            `Metadata for "${sample_id}"`);
    });

    d3.json("/samples/" + query_sample_id, function (error, response) {
        let sample_id = parseInt(query_sample_id.split("_")[1]).pad(4);
        // console.log("Response from /samples/" + query_sample_id, response);
        if (error) return console.warn(error);

        //  render pie chart
        render_pie_chart(
            "bb-pie-chart",
            response["value"],
            response["id"],
            response["label"],
            `Top-10 Sample counts for "${sample_id}"`);

        // render bubble plot
        render_bubble_plot(
            "bb-bubble-plot",
            response["id"],
            response["value"],
            response["label"],
            `Top-10 Sample counts for "${sample_id}"`)
    });

    d3.json("/wfreq/" + query_sample_id, function(error, response){
        let sample_id = parseInt(query_sample_id.split("_")[1]).pad(4);
        if (error) return console.warn(error);

        render_gauge_chart(
            "wfreq-gauge-chart",
            response,
            `Washing frequency per week for "${sample_id}"`);

    })


}

function sample_handler(element) {
   let query_sample_id =  "bb_" + parseInt(element.target.value);
   render_index(query_sample_id);
}

render_index("bb_940");



let $sampleInput =  document.getElementById("bb-form-input");
// add event listener to sample input drop-down
$sampleInput.addEventListener("change", sample_handler)
// var query_sample_id = "bb_" + parseInt($sampleInput.value);
// console.log(query_sample_id);


