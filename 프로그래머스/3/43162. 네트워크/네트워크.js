function solution(n, computers) {
    var answer = 0;
    var graph = new Array(n).fill().map(() => []);
    
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (computers[i][j] == 1) {
                if ([...graph[i]].includes(j) == false) {
                    graph[i].push(j);
                } 
                if ([...graph[j]].includes(i) == false) {
                    graph[j].push(i);
                }
            }
        }
    }
    
    var visited = new Array(n).fill(0);
    for (i = 0; i < n; i++) {
        console.log(i, visited[i], graph[i]);
        if (visited[i] == 0) {
            answer += 1;
            connectedComputers = [...graph[i]];
            while (connectedComputers.length > 0) {
                curr = connectedComputers.pop();
                visited[curr] = 1;
                adjacents = graph[curr];
                for (let v of adjacents) {
                    if (visited[v] == 0) {
                        connectedComputers.push(v);
                    }
                }
            }
        }
    }
    return answer;
}