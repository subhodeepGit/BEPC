// frappe.pages['bi-report'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'None',
// 		single_column: true
// 	});
// }

frappe.pages['bi-report'].on_page_load = function(wrapper) {
	new PageContent(wrapper);
};

PageContent = Class.extend({
	init:function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Equipment uptime and downtime report',
			single_column: true
		});

		this.make();
	},

	make: function(){
		let htmlContent = `

		<head>
    <style>
        /* .container {
            position: relative;
            background-color: blue;
            height: 100%;
            width: 100%;
            border: 1px solid;
            color: white;
            background-color: #cccccc;
        } */

        .header {
            position: absolute;
            margin-top: 5px;
            background-color: #5a5658;
            left: 0;
            right: 0;
            height: 54px;
            width:1465px;
            margin-left: 18px;
            padding: 8px;
            font-size: large;
        }
        
    </style>
</head>
		
<body> 
<div class="header"></div>
<iframe src="http://10.0.136.19:5000/"
        style="height: 100vh; width: 80vw;border: 1px solid white; box-shadow: 0 0 5px black;">
</iframe>
		
</body>		
		`
		;

		$(frappe.render_template( htmlContent, this )).appendTo(this.page.main)
	},

});

{/* <iframe class="embed-responsive-item" src="https://app.powerbi.com/view?r=eyJrIjoiYTgxN2NjMjQtMmY0Ny00ZDk5LWE5YmYtMDYxMjUzZWMzNzYxIiwidCI6IjYxZDFmOTk1LTkxMjgtNDhmYy1iNmFlLWE2ZDI3ZTBkZGJkMSJ9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe> */}

{/* <iframe class="embed-responsive-item" src="https://soulunileaders.com/" ></iframe> */}