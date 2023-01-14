import * as server from "https://deno.land/std@0.168.0/http/server.ts";

// * Function to handle CTL-C *
function sigIntHandler() : void {
    console.log( "\n%cInterrupted!", "color: red; font-weight: bold");
    Deno.exit();
}
Deno.addSignalListener("SIGINT", sigIntHandler);

// * Server Handler *
// Handler Variables
const Book_route = new URLPattern({pathname: "/"});

// Handler Function
async function handler(req: Request): Promise<Response> {
    const match: URLPatternResult | null = Book_route.exec(req.url);
    let response: Response;

    // if route matches
    if (match) {
        const body:string = await Deno.readTextFile("test.html")
        response = new Response(body);
    }
    // else return 404
    else {
        response = new Response("<h1>404: Page Not found :(</h1>", {
            status: 404,
        });
    }
    response.headers.set("content-type", "text/html");
    return response;
}

//  * Main Server Script *
console.log("%c✔ - Server Running", "color: green");
server.serve(handler);