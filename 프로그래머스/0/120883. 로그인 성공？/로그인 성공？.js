function solution(id_pw, db) {
    var answer = "fail";
    let id = id_pw[0];
    let pw = id_pw[1];
    
    db.forEach(([db_id, db_pw]) => {
        if (id == db_id) {
            if (pw == db_pw) {
                answer = "login"
            } else {
                answer = "wrong pw"
            }
        }
    })
    return answer;
}