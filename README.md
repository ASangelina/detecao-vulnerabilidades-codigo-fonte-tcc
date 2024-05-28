# detecao-vulnerabilidades-codigo-fonte-tcc



## Dados
|   # |   label | code                                                                                                   |   cbo |   cboModified |   fanin |   fanout |   wmc |   dit |   noc |   rfc |   lcom |   lcom* |   tcc |   lcc |   totalMethodsQty |   staticMethodsQty |   publicMethodsQty |   privateMethodsQty |   protectedMethodsQty |   defaultMethodsQty |   visibleMethodsQty |   abstractMethodsQty |   finalMethodsQty |   synchronizedMethodsQty |   totalFieldsQty |   staticFieldsQty |   publicFieldsQty |   privateFieldsQty |   protectedFieldsQty |   defaultFieldsQty |   finalFieldsQty |   synchronizedFieldsQty |   nosi |   loc |   returnQty |   loopQty |   comparisonsQty |   tryCatchQty |   parenthesizedExpsQty |   stringLiteralsQty |   numbersQty |   assignmentsQty |   mathOperationsQty |   variablesQty |   maxNestedBlocksQty |   anonymousClassesQty |   innerClassesQty |   lambdasQty |   uniqueWordsQty |   modifiers |   logStatementsQty |
|-------------:|--------:|:-------------------------------------------------------------------------------------------------------|------:|--------------:|--------:|---------:|------:|------:|------:|------:|-------:|--------:|------:|------:|------------------:|-------------------:|-------------------:|--------------------:|----------------------:|--------------------:|--------------------:|---------------------:|------------------:|-------------------------:|-----------------:|------------------:|------------------:|-------------------:|---------------------:|-------------------:|-----------------:|------------------------:|-------:|------:|------------:|----------:|-----------------:|--------------:|-----------------------:|--------------------:|-------------:|-----------------:|--------------------:|---------------:|---------------------:|----------------------:|------------------:|-------------:|-----------------:|------------:|-------------------:|
|            0 |       0 | private List<AuthInfo> createAuthInfo(SolrZkClient zkClient) {                                         |     5 |             5 |       0 |        5 |     2 |     1 |     0 |     6 |      0 |       0 |    -1 |    -1 |                 1 |                  0 |                  0 |                   1 |                     0 |                   0 |                   0 |                    0 |                 0 |                        0 |                0 |                 0 |                 0 |                  0 |                    0 |                  0 |                0 |                       0 |      0 |    10 |           1 |         1 |                0 |             0 |                      0 |                   0 |            0 |                2 |                   0 |              2 |                    1 |                     0 |                 0 |            0 |               13 |           1 |                  0 |
|              |         |       List<AuthInfo> ret = new LinkedList<AuthInfo>();                                                 |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |                                                                                                        |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |       // In theory the credentials to add could change here if zookeeper hasn't been initialized       |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |       ZkCredentialsProvider credentialsProvider =                                                      |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |         zkClient.getZkClientConnectionStrategy().getZkCredentialsToAddAutomatically();                 |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |       for (ZkCredentialsProvider.ZkCredentials zkCredentials : credentialsProvider.getCredentials()) { |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |         ret.add(new AuthInfo(zkCredentials.getScheme(), zkCredentials.getAuth()));                     |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |       }                                                                                                |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |       return ret;                                                                                      |       |               |         |          |       |       |       |       |        |         |       |       |                   |                    |                    |                     |                       |                     |                     |                      |                   |                          |                  |                   |                   |                    |                      |                    |                  |                         |        |       |             |           |                  |               |                        |                     |              |                  |                     |                |                      |                       |                   |              |                  |             |                    |
|              |         |     }   
