 This repository is an implementation of [Ostorlab Agent](https://pypi.org/project/ostorlab/) for the [snallygaster tool](https://github.com/hannob/snallygaster).  
  ## Getting Started  
  To perform your first scan, simply run the following command:  
  ```shell  
  ostorlab scan run --install --agent agent/mohsinenar/snallygasterdomain-name sub.domain.com  
  ```  
  ## Installation & Usage  
    
    
   ### Install directly from ostorlab agent store  
   ```shell  
   ostorlab agent install agent/mohsinenar/snallygaster 
   ```  
  You can then run the agent with the following command:  
  ```shell  
  ostorlab scan run --agent agent/mohsinenar/snallygasterdomain-name sub.domain.com  
  ```  
  ### Build directly from the repository  
   1. To build the nmap agent you need to have [ostorlab](https://pypi.org/project/ostorlab/) installed in your machine.  if you have already installed ostorlab, you can skip this step.  
  ```shell  
  pip3 install ostorlab  
  ```  
   2. Clone this repository.  
  ```shell  
  git clone https://github.com/mohsinenar/agent_dns_reaper.git && cd agent_snallygaster 
  ```  
   3. Build the agent image using ostorlab cli.  
   ```shell  
   ostortlab agent build --file=ostorlab.yaml  
   ```  
   You can pass the optional flag `--organization` to specify your organisation. The organization is empty by default.  
   4. Run the agent using on of the following commands:  
     * If you did not specify an organization when building the image:  
      ```shell  
      ostorlab scan run --agent agent//snallygasterip 8.8.8.8  
      ```  
     * If you specified an organization when building the image:  
      ```shell  
      ostorlab scan run --agent agent/[ORGANIZATION]/snallygasterip 8.8.8.8  
      ```

  ## License
  [Apache-2.0](./LICENSE)

#References
- [Ostorlab](https://pypi.org/project/ostorlab/)
- [Ostorlab docs](https://docs.ostorlab.co/tutorials/run-your-first-scan/)
- [snallygaster](https://github.com/hannob/snallygaster).  