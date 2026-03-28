document.addEventListener("DOMContentLoaded", function () {

  fetch('/api/result')  // 🔥 Better endpoint than /api/submit
    .then(res => res.json())
    .then(data => {

      // Career + Score
      document.getElementById("career-title").textContent = data.career;
      document.getElementById("score-value").textContent = data.score + "%";
      document.getElementById("score-bar").style.width = data.score + "%";

      // Split skills into categories
      let techHTML = "";
      let softHTML = "";

      for (let skill in data.skills) {
        let value = data.skills[skill];

        let block = `
          <div class="skill-row">
            <p>${skill} <span>${value}%</span></p>
            <div class="progress-bar">
              <div class="progress" style="width:${value}%"></div>
            </div>
          </div>
        `;

        // Simple classification logic
        if (["Python", "SQL", "Data Vis"].includes(skill)) {
          techHTML += block;
        } else {
          softHTML += block;
        }
      }

      document.getElementById("technical-skills").innerHTML = techHTML;
      document.getElementById("soft-skills").innerHTML = softHTML;

      // Gaps
      let gapHTML = "";
      data.gaps.forEach(g => {
        gapHTML += `<li>${g}</li>`;
      });

      document.getElementById("gap-list").innerHTML = gapHTML;

    })
    .catch(err => {
      console.error(err);
      document.getElementById("career-title").textContent = "Error loading result";
    });

});