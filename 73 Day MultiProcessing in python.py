# Day 73 -> MultiProcessing in python


import multiprocessing
import requests
import concurrent.futures


def downloadfile(url, name):
    print(f"start downloading {name}")
    response= requests.get(url)
    open(f"files/{name}.jpg", "wb").write(response.content)
    print("finished {name}")


if __name__ == "__main__":  # Required for Windows
    url = [
        "https://w0.peakpx.com/wallpaper/552/240/HD-wallpaper-gaming-wiki-good-gaming.jpg",
        "https://e0.pxfuel.com/wallpapers/502/926/desktop-wallpaper-wiki-cool-2560x1080.jpg",
        "https://www.nicepng.com/png/detail/850-8504261_deadpool-fox-battles-wiki-fandom-powered-wikia-deadpool.png"
    ]

    # pros = []
    # for i in range(3):
    #     p = multiprocessing.Process(target=downloadfile, args=(url[i], i))
    #     p.start()
    #     pros.append(p)

    # for q in pros:
    #     q.join()
    
    l1 = url 
    l2= list(range(len(url)))

    with concurrent.futures.ProcessPoolExecutor() as executor :
    
        results = executor.map(downloadfile, l1, l2 )
        for r in results:
            print(r)
     