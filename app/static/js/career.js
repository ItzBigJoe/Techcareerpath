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
        if (skill === "Readiness") continue; // Skip overall readiness in detailed view
        
        let value = data.skills[skill];

        let block = `
          <div class="skill-row">
            <p>${skill} <span>${value}%</span></p>
            <div class="progress-bar">
              <div class="progress" style="width:${value}%"></div>
            </div>
          </div>
        `;

        // Detailed classification logic
        const techCategories = ["Frontend", "Backend", "AI/Data Science", "DSA", "Technical"];
        if (techCategories.includes(skill)) {
          techHTML += block;
        } else if (skill === "Soft Skills") {
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